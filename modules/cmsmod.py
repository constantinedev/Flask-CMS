import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, asyncio, pytz, pgpy, jwt, base64, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort, send_from_directory
import pycountry, pyotp, qrcode, qrcode.constants
from qrcode.image.svg import SvgFillImage, SvgPathFillImage, SvgPathImage

async def QueryFunction():
	json_data = {
		"status": 200,
		"response": "Query Function Ready Connect"
	}
	return jsonify(json_data), 200

#########
### The System Core Functions
### Upgrade your design better then me :)

async def FX_2FA(user_token):
	totp_auth = pyotp.totp.TOTP(user_token).provisioning_uri(
		name="Delete Me when debug",
		issuer_name = "Custom 2FA"
	)
	qrIMAGE = await svgQRmaker(totp_auth)
	return qrIMAGE

async def jwtMaker(token, phass):
  jsonData = {
    "data":token,
    "exp": DT.now(TZ.utc) + TD(minutes=15)
  }
  encoded = jwt.encode(jsonData, phass, algorithm="HS512")
  return encoded

async def jwtRecovery(Str, phass):
  data = jwt.decode(Str, phass, algorithms=["HS512"])
  return data

async def tokMaker(uname_, phass_):
	if uname_ is not None and phass_ is not None:
		uname = base64.b16encode(str(uname_).encode("UTF-8")).decode("UTF-8")
		phass = base64.b16encode(str(phass_).encode("UTF-8")).decode("UTF-8")
		token = f"{uname}:{phass}"
		return token
	else:
		return abort(404)
	
async def tokRecovery(token):
	uname_, phass_ = str(token).strip(":")
	uname = base64.b16decode(uname_.encode("UTF-8"))
	phass = base64.b16decode(phass_.encode("UTF-8"))
	return uname, phass
	
async def pgpEnc(data, phass):
	pgpMsg = pgpy.PGPMessage.new(data).encrypt(phass)
	return pgpMsg
	
async def pgpDec(data, phass):
	txtMsg = pgpy.PGPMessage.from_blob(data).decrypt(phass).message
	return txtMsg

async def svgQRmaker(src):
	qr = qrcode.QRCode(version=5, box_size=10, border=0, error_correction=qrcode.constants.ERROR_CORRECT_L, image_factory=SvgPathFillImage)
	qr.add_data(src)
	qr.make(fit=True)
	img = qr.make_image(attrib={'class': 'vQR'})
	svgImg = img.to_string(encoding="unicode")
	return svgImg

async def CountryList():
  countryList = []
  all_countrys = pycountry.countries
  for country in all_countrys:
    timezones = pytz.country_timezones.get(country.alpha_2)
    if timezones:
      for timezone in timezones:
        offset = DT.now(pytz.timezone(timezone)).strftime("%z")
        offset = f"{offset[:-2]}:{offset[-2:]}"
        _da = {
          "country_code": country.alpha_2,
          "timezone_offset": offset,
          "country_name": country.name,
          "timezone": timezone,
        }
        countryList.append(_da)
      else:
        pass
  return jsonify(countryList), 200