import re, os, io, json, sqlite_utils, requests, logging
from sqlite_utils.utils import sqlite3
from datetime import datetime as DT, timezone as TZ
from flask import Flask, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from system.setup import agent, login

def set_password(password):
  return generate_password_hash(password, method="pbkdf2:sha256")
  
def check_password(login_id, password):
  for row in list(sqlite_utils.Database('db/admin.session')['agents'].rows_where("login_id = :login_id", {"login_id": login_id})):
    return check_password_hash(row['pwd'], password)

def register():
  if request.method == 'POST':
    UID = request.form['UID']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    fname = request.form['fname']
    lname = request.form['lname']

    for row in list(sqlite_utils.Database('db/admin.session')["vlogin"].rows_where("login_id = :UID", {"UID": UID})):
      return render_template('register.html', title="ERROR", username_err="UserID Already Registed!")
    for row in list(sqlite_utils.Database('db/admin.session')['vlogin'].rows_where("email = :email", {"email": email})):
      return render_template('register.html', title="ERROR", email_err="E-mail Already Registed!")
    for row in list(sqlite_utils.Database('db/admin.session')['vlogin'].rows_where("username = :username", {"username": username})):
      return render_template('register.html', title="ERROR", dpname_err="E-mail Already Registed!")

    pwd_hash = set_password(password)
    reg_info = {
      "login_id": UID,
      "pwd": pwd_hash,
      "username": username,
      "email": email,
      "fname": fname,
      "lname": lname,
      "create_dateime": str(DT.now(TZ.utc))
    }

    try:
      sqlite_utils.Database('db/admin.session')['agents'].insert(reg_info, alter=True)
      return redirect('/login')
    except:
      return render_template('theam/register.html', title="ERROR", result="REGIST ERROR")
  
  if request.method == 'GET':
    return render_template('theam/register.html', title='REGISTER')

def sing_in():
  if current_user.is_authenticated:
    return redirect('/panel')
      
  if request.method == 'POST':
    login_id = request.form['username']
    pwd = request.form['password']
    if login_id is not None and check_password(request.form['username'], pwd):
      loginID = agent()
      loginID.id = request.form['username']
      login_user(loginID)
      
      return redirect('/panel')
    else:
      return render_template('theam/login.html', pwd_err="Wrong Password OR Login ID")
  
  return render_template(
    'theam/login.html',
    title='LOGIN',
    pag='panel',
  )

def sing_out():
  logout_user()
  return redirect('/')

### GET REQUEST RETURN
def panel_api():
  pag = request.args.get("pag")
  model_ = request.args.get('mod')
  act_ = request.args.get('act_')
  
  if request.method == "GET":
    ### FROM GET REQUEST
    if pag == "agent_manage":
      agents = []
      for users_ in list(sqlite_utils.Database("db/admin.session")['agents'].rows):
        agents.append(users_)
      return render_template('admin/panel.html', title="PANEL", pag=pag, agents_lst=agents, agents_count=int(len(agents)))

    if pag == "categorys_edit":
      categorys = []
      act_ = request.args.get('act_')
      if act_ == "act_list":
        for row in list(sqlite_utils.Database('data_db/blog.sqlite3')['categories'].rows):
          categorys.append(row)
        return render_template("admin/panel.html", pag=pag, title='CATEGORY EDITOR', cat_lst=categorys, cat_len=int(len(categorys)))
    
      if act_ == "get":
        cat_id = request.args.get("cat_id")
        for row in list(sqlite_utils.Database('data_db/blog.sqlite3')['categories'].rows_where("id = :cat_id", {"cat_id": cat_id})):
          categorys.append(row)
        return jsonify(categorys[0])
    
    if pag == "categorys":
      return categorys_edit()

  if request.method == "POST":
    ### FROM POST REQUEST
    if model_ == "settings":
      if pag == "categorys_edit":
        return categorys_edit()
      
      if act_ == 'profileupdate':
        return profile_update_()

      if act_ == 'get_age_pro':
        userid = request.args.get('user_id')
        return get_agents_profile(userid)

      if act_ == 'agent_edit':
        return update_users()
      
    if model_ == "imgupdload":
      return img_uploader()
  
  return render_template('admin/panel.html', title="PANEL", pag=pag)

### JavaScript Return Formate
def get_agents_profile(userid):
  asg_api = {}
  for agent in sqlite_utils.Database('db/admin.session')['agents'].rows_where("id = :id", {"id": userid}):
    asg_api.update(agent)
    return jsonify(asg_api)
###############################

def profile_update_():  
    old_pwd = request.form['old-password']
    new_pwd = request.form['new-password']

    if old_pwd is None or old_pwd == "":
      return_log = 'No Password Inputed!'
      return render_template('admin/panel.html', title="PANEL", pag="profile", return_log=return_log)

    if new_pwd is None :
      password_fix = request.form['new-password']
    else:
      password_fix = request.form['old-password']

    if check_password(request.form['loginID'], request.form['old-password']):
      prof_upd_reg = {
        # "login_id": request.form['loginID'],
        "pwd": set_password(password_fix),
        "email": request.form['email'],
        "username": request.form['dpName'],
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "last_update": str(DT.now(TZ.utc))
      }
      try:
        sqlite_utils.Database('db/admin.session')['agents'].update(current_user.id, prof_upd_reg, alter=True)
        flash("PROFILE UPDATE SECCESS")
        return render_template('admin/panel.html', title="PANEL", pag="profile")
      except sqlite3.OperationalError as e:
        flash(f"UPDATE Error: {e}")
        return render_template('admin/panel.html', title="PANEL", pag="profile")
    else:
      flash("Password Not Match!")
      return render_template('admin/panel.html', title="PANEL", pag="profile")

def update_users():
  for agent in list(sqlite_utils.Database('db/admin.session')['agents'].rows_where("login_id = :loginID", {"loginID": request.json['login_id']})):
    try:
      sqlite_utils.Database('db/admin.session')['agents'].update(agent['id'], request.json, alter=True)
      return jsonify({"status": f"UPDATE SUCCESS"})
    except sqlite3.IntegrityErrir as e:
      return jsonify({"status": f"UPDATE ERROR: {e}"})
      
  return redirect(url_for("panel", pag="agent_manage", title="POST COMPLET"))

def categorys_edit():
  # order_act = request.args.get('acts_')
  
  if request.args.get('acts_') == 'add':
    data = request.get_json()
    categorys_data = {
      "name": data['name'],
      "link": data['link'],
      "description": data['desc_'],
      "laste_edit": current_user.login_id,
      "create_date": str(DT.now(TZ.utc)),
    }
    try:
      sqlite_utils.Database("data_db/blog.sqlite3")['categories'].insert(categorys_data, alter=True)
      return jsonify({"status": "CREATE SUCCESS"})
    except sqlite3.IntegrityError as e:
      return jsonify({"status": "CATEGORY ALREADY EXISTS"})
      
  if request.args.get('acts_') == 'update':
    data = request.get_json()
    categorys_data = {
      "name": data['name'],
      "link": data['link'],
      "description": data['desc_'],
      "laste_edit": current_user.login_id,
      "last_update": str(DT.now(TZ.utc)),
    }    
    try:
      sqlite_utils.Database("data_db/blog.sqlite3")['categories'].update(request.args.get('id'), categorys_data, alter=True)
      # flash('UPDATE SUCCESS')
      return jsonify({"status": "UPDATE SUCCESS"})
    except sqlite3.OperationalError as e:
      # flash('UPDATE ABORT')
      return jsonify({"status": f"UPDATE ABORT: {e} "})
    
  if request.args.get('acts_') == 'remove':
    data = request.get_json()
    categorys_data = {
      "id": data['id'],
    }    
    try:
      sqlite_utils.Database("data_db/blog.sqlite3")['categories'].delete(int(data['id']))
      # flash('UPDATE SUCCESS')
      return redirect('/panel?mod=categorys_edit&act_=act_list')
    except sqlite3.OperationalError as e:
      # flash('UPDATE ABORT')
      return jsonify({"status": f"DELETE ABORT: {e} "})
      
  return redirect("/panel?mod=categorys_edit&act_=act_list")

from PIL import Image
def img_uploader():
  file = request.files.get('file')
  if file:
        filename = file.filename.lower()
        fn, ext = filename.split('.')
        # truncate filename (excluding extension) to 30 characters
        fn = fn[:30]
        filename = fn + '.' + ext
        if ext in ['jpg', 'gif', 'png', 'jpeg']:
            try:
                # everything looks good, save file
                img_fullpath = os.path.join('static/uploads/', filename)
                file.save(img_fullpath)
                # get the file size to save to db
                file_size = os.stat(img_fullpath).st_size
                size = 1024, 512
                # read image into pillow
                im = Image.open(img_fullpath)
                # get image dimension to save to db
                file_width, file_height = im.size
                # convert to thumbnail
                im.thumbnail(size)
                thumbnail = fn + '-thumb.jpg'
                tmb_fullpath = os.path.join('static/uploads/', thumbnail)
                # PNG is index while JPG needs RGB
                if not im.mode == 'RGB':
                    im = im.convert('RGB')
                # save thumbnail
                im.save(tmb_fullpath, "JPEG")

                # save to db
                img_data = {
                  "fileanem": filename,
                  "thumbnail": thumbnail,
                  "file_size": file_size,
                  "file_width": file_width,
                  "file_height": file_height
                  
                }
                try:
                  sqlite_utils.Database('data_db/blog.sqlite3')['img_db'].insert(img_data, alter=True)
                  flash("IMG UPLOAD SUCCESS")
                except sqlite3.InterruptedError as e :
                  flash(f'IMG UPLOAD ERROR: {e}')
                
            except IOError:
                return Response('Cannot create thumbnail for ' + filename, 500)
            return jsonify({'location' : filename})

    # fail, image did not upload
  return Response('Filename needs to be JPG, JPEG, GIF or PNG', 500)
