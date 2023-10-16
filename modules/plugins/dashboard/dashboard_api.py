import re, io, os, sys, ast, json, sqlite_utils, logging, pgpy
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort

async def page_loader():
  if request.method == "GET":
    pag = request.args.get('pag')
    if pag == "" or pag=="dashboard":
      return render_template('plugins/dashboard/main.htm', pag="dashboard", title="Dashboard")
    else:
      return render_template('plugins/dashboard/main.htm', pag=pag, title="Dashboard")
