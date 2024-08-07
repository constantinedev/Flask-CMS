import re, io, os, sys, ssl, ast, csv, json, base64, sqlite_utils, pgpy, logging
from datetime import datetime as DT, timezone as TZ, timedelta as TD
from sqlite_utils.utils import sqlite3
from flask import Flask, Blueprint, request, Response, make_response, render_template, jsonify, redirect, url_for, abort, flash, send_from_directory
from modules.aioRequests import gun_shell

from system.panel import panel_api
from modules.plugins.dashboard.dashboard_api import dashboard_panel

async def page_loader(page):
    if page == "" or page is None:
      return render_template('layout.html', pag='home', title='Home')
    if page == 'dashboard':
      return await dashboard_panel(page)
    if page == 'panel':
      return await panel_api()
    else:
      return redirect(f'/?pag={page}')