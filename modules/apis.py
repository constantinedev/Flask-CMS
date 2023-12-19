import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, asyncio, pytz, pgpy, base64, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort, send_from_directory

from modules.aioRequests import gun_shell

async def api_loader(version):
  if request.method == "GET":
    if version == "v1":
      return await api_v1()
    elif version == "v2":
      return await api_v2()
    else:
      return jsonify({"status": "Normal Connect Success!"})
  elif request.method == "POST":
    if version == "v2":
      return await api_v2()
    elif request.args.get("mod") == "sq":
      return await QueryFunction()
    else:
      return redirect('/error_page')
      
async def api_v1():
  return jsonify({"status": 200, "response": "API v1 test comport"}), 200

async def api_v2():
  return jsonify({"status": 200, "response": "API v2 test comport"}), 200

async def QueryFunction():
  json_data = {
    "status": 200,
    "response": "Query Function Ready Connect"
  }
  return jsonify(json_data), 200

async def tokMaker(uname_, phass_):
  if uname_ is not None and phass_ is not None:
    uname = base64.b16decode(uname_.encode("UTF-8")).decode("UTF-8")
    phass = base64.b16decode(phass_.encode("UTF-8")).decode("UTF-8")
    token = f"{uname}:{phass}"
    return token
  
async def pgpEnc(data, phass):
  pgpMsg = pgpy.PGPMessage.new(data).encrypt(phass)
  return pgpMsg
  
async def pgpDec(data, phass):
  txtMsg = (data).decrypt(phass).message
  return txtMsg