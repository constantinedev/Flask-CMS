import re, os, io, json, sqlite_utils, requests, logging
from sqlite_utils.utils import sqlite3
from datetime import datetime as DT , timezone as TZ
from flask import Flask, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from flask_ckeditor import CKEditor, upload_success, upload_fail
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
ckeditor = CKEditor(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['CKEDITOR_PKG_TYPE'] = 'full-all'
app.config['CKEDITOR_FILE_UPLOADER'] = 'uploads'

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
def user_conf(config):
  if request.method == "POST":
    if config == 'update_profile':
      print('demo')
    return 'TEST Today' + str(DT.now())

# @app.route('/files/<path:filename>')
# def uploaded_files(filename):
#     path = '/the/uploaded/directory'
#     return send_from_directory(path, filename)

# @app.route('/upload', methods=['POST'])
# def upload():
#     f = request.files.get('upload')
#     # Add more validations here
#     extension = f.filename.split('.')[-1].lower()
#     if extension not in ['jpg', 'gif', 'png', 'jpeg']:
#         return upload_fail(message='Image only!')
#     f.save(os.path.join('/the/uploaded/directory', f.filename))
#     url = url_for('uploaded_files', filename=f.filename)
#     return upload_success(url, filename=f.filename)  # return upload_success call

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8001, debug=True)
