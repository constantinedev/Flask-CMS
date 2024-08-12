import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, asyncio, pytz, pgpy, jwt, base64, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort, send_from_directory
import pycountry, pyotp, qrcode, qrcode.image.svg, qrcode.constants

from modules.cmsmod import pgpEnc, pgpDec, jwtMaker, jwtRecovery, tokMaker, tokRecovery, FX_2FA, CountryList, QueryFunction, svgQRmaker
from modules.aioRequests import gun_shell

async def api_loader(version):
  if request.method == "GET":
    if version == "v1":
      return await api_v1()
    else:
      return jsonify({"status": 200, "response": "Page Not Found!"}), 200
  elif request.method == "POST":
    if version == "v2":
      return await api_v2()
    else:
      return abort(404)
      
async def api_v1():
  reqType = request.args.get('info')
  if reqType == "ctzinfo":
    return await CountryList()
  return jsonify({"status": 200, "response": "API v1 test comport"}), 200

async def api_v2():
  if request.args.get('mod') == "sq":
    return await QueryFunction()
  return jsonify({"status": 200, "response": "API v2 test comport"}), 200