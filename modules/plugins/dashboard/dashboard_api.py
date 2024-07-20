import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, pytz, pgpy, base64, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort

async def page_loader(page):
	if request.method == "GET":
		if page=="dashboard":
			return render_template('plugins/dashboard/main.htm', pag="dashboard", title="Dashboard")
		elif page == "home" or page == "" or page is None:
			return render_template('layout.html', pag='home', title="Dashboard")
		else:
			return redirect(f'/?pag={page}')

	if request.method == "POST":
		apis = request.args.get('apis')
		if apis == "" or apis is None:
			return redirect(url_for("/error_page"))
		else:
			retu_json = request.get_json()
			return jsonify(retu_json), 200
