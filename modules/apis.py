import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, asyncio, pytz, pgpy, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort, send_from_directory

from modules.aioRequests import gun_shell

async def api_loader(version):
  if request.method == "GET":
    if version == "v1":
      await api_v1()
    else:
      return jsonify({"status": "Normal Connect Success!"})
  elif request.method == "POST":
    if version == "v2":
      await api_v2()
    if request.args.get("mod") == "sq":
      await QueryFunction()
      
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