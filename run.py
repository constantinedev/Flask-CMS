import re, os, io, json, sqlite_utils, requests, logging
from sqlite_utils.utils import sqlite3
from datetime import datetime as DT , timezone as TZ
from flask import Flask, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from werkzeug.middleware.proxy_fix import ProxyFix
from system.setup import login
from system.panel import set_password, check_password, panel_api, register, sing_in, sing_out, img_uploader

from modules.plugins.blogger.blog import blog_api

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

app = Flask(__name__)
app.secret_key = b'82d52ae6cdbed60d2e6923b0b562f99adab07c6d6b57a55c5e2f4043ebde05d2'
app.wsgi_app = ProxyFix(app.wsgi_app)

if app.testing:
    app.config['WTF_CSRF_ENABLED'] = False
    
login.init_app(app)
login.login_view = '/login'

@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == 'GET':
    pag = request.args.get('pag')
    if pag is not None:
      return render_template('layout.html', pag=pag)
    else:
      return render_template('layout.html', pag="home")

@app.errorhandler(404)
def error_page(error):
  return render_template("error.html", title=error), 404

### REGISTER
@app.route('/regist', methods=["GET", "POST"])
def reg_ac():
  return register()
  
### LOGIN
@app.route('/login', methods=["GET", "POST"])
def log_in():
  return sing_in()
  
### LOG OUT
@app.route('/logout')
def log_out():
  return sing_out()

### CLT PANEL
@app.route('/panel', methods=["GET", "POST"])
@login_required
def panel():
    return panel_api()

@app.route('/panel/blogger', methods=["GET", "POST"])
@login_required
def blogger_mod():
  return blog_api()

### CMS PANEL API
@app.route('/settings/<config>', methods=["GET", "POST"])
@login_required
def user_conf(config):
  if request.method == "POST":
    if config == 'update_profile':
      print('demo')
    return 'TEST Today' + str(DT.now())

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8001, debug=True)
