import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, asyncio, pytz, pgpy, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort, send_from_directory

from modules.aioRequests import gun_shell

async def api_loader():
  if request.method == "GET":
    if request.args.get("mod") == "":
      await apis()
    else:
      return jsonify({"status": "Normal Connect Success!"})
  elif request.method == "POST":
    if request.args.get("mod") == "sq":
      await QueryFunction()
      
async def apis():
  json_data = {
    "status": "Success",
    "response": "apis redirect complete."
  }
  return jsonify(json_data), 200

async def QueryFunction():
  json_data = {
    "status": 200,
    "response": "Query Function Ready Connect"
  }
  return jsonify(json_data), 200