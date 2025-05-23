import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, pytz, pgpy, base64, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort
from flask_login import current_user

from modules.cmsmod import pgpEnc, pgpDec, jwtMaker, jwtRecovery, tokMaker, tokRecovery, FX_2FA, CountryList, QueryFunction, svgQRmaker

async def dashboard_panel(page):
	info = request.args.get('info')
	mod = request.args.get('mod')

	if request.method == "GET":
		if current_user.is_authenticated:
			if page == 'dashboard':
				content = render_template('plugins/dashboard/main.htm', pag="dashboard", title="Dashboard")
				response = make_response(content)
				response.headers['token'] = current_user.token
				return response
		else:
			return redirect(f'/')

	if request.method == "POST":
		pag = request.args.get('pag')
		
		#####
		### Function response on POST start here
