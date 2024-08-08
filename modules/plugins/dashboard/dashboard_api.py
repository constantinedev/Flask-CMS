import re, io, sys, os, ast, ssl, csv, json, requests, sqlite_utils, pytz, pgpy, base64, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort
from flask_login import current_user

async def dashboard_panel(page):
	if current_user.is_authenticated:
		content = render_template('plugins/dashboard/main.htm', pag="dashboard", title="Dashboard")
		response = make_response(content)
		response.headers['token'] = current_user.token
		return response
	else:
		content = render_template('plugins/dashboard/main.htm', pag="dashboard", title="Dashboard")
		response = make_response(content)
		return response