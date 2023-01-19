import re, os, io, json, sqlite_utils, requests, logging
from sqlite_utils.utils import sqlite3
from datetime import datetime as DT, timezone as TZ
from flask import Flask, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from system.setup import agent, login

def blog_api():
  pag = request.args.get('pag')
  mod = request.args.get('mod')
  act_ = request.args.get('act_')
  
  agents = []
  for users_ in list(sqlite_utils.Database("db/admin.session")['agents'].rows):
    agents.append(users_)
  
  if request.method == "GET":
    ###GET REQUEST
    if pag == 'crt_newpost':
      return get_create_info(pag)
    
    if pag == 'post_edit':
      return post_lst(pag)
    
    if pag == 'post_review':
      return post_review(request.args.get('post_id'))
    
  if request.method == "POST":
    ### POST REQUEST
    if mod == "modify":
      if request.args.get('act_') == 'crt_newpost':
        return post_create()
    
      if request.args.get('act_') == 'update_post':
        return post_update()
      
      if request.args.get('act_') == 'remove':
        return remove_post()
  
  return render_template('admin/panel.html', title="PANEL", pag=pag, agents_lst=agents, agents_count=int(len(agents)))

def get_create_info(pag):
  categorys_lst = []
  agents_lst = []
  
  for categorys in list(sqlite_utils.Database("data_db/blog.sqlite3")['categories'].rows):
    categorys_lst.append(categorys)
  for agents in list(sqlite_utils.Database('db/admin.session')['vlogin'].rows):
    agents_lst.append(agents)
  return render_template('admin/panel.html', pag=pag, title="CREATE NEW POST", categorys_lst=categorys_lst, categorys_len=int(len(categorys_lst)), agents_lst=agents_lst, agents_len=int(len(agents_lst)))

def post_lst(pag):
  post_lst = []
  categorys_lst = []
  agents_lst = []
  
  for posts in list(sqlite_utils.Database('data_db/blog.sqlite3')['post'].rows):
    post_lst.append(posts)
  for categorys in list(sqlite_utils.Database("data_db/blog.sqlite3")['categories'].rows):
    categorys_lst.append(categorys)
  for agents in list(sqlite_utils.Database('db/admin.session')['vlogin'].rows):
    agents_lst.append(agents)
  return render_template('admin/panel.html', pag=pag, title="POST EDITOR", post_lst=post_lst, post_len=int(len(post_lst)), categorys_lst=categorys_lst, categorys_len=int(len(categorys_lst)), agents_lst=agents_lst, agents_len=int(len(agents_lst)))

def post_review(post_id):
  post = []
  post_ = sqlite_utils.Database('data_db/blog.sqlite3')['post'].get(int(post_id))
  post.append(post_)
  
  return jsonify(post[0])

### CREATE POST
def post_create():
  new_post_data = {
		"status": request.form['status'],
		"publish_date": request.form['publish-date'],
		"title": request.form['post-title'],
		"author": request.form['author'],
		"content": request.form['post-content'],
		"categories": request.form['categories'],
		"tag": request.form['tag'],
		# "lnk": request.form['link'],
		"crt_agent": current_user.dpName,
		"crt_date": str(DT.now(TZ.utc)),
	}
  
  try:
    sqlite_utils.Database('data_db/blog.sqlite3')['post'].insert(new_post_data, alter=True)
    flash("!!!New Post Complate Create!!!")

  except sqlite3.OperationalError as e:
    flash(f"!!!{e}!!!")
    
  return redirect(url_for("blogger_mod", mod="blogger", pag='crt_newpost', title="CREATE POST"))


def post_update():
  post_id = int(request.form['postID'])
  upd_post_data = {
		"status": request.form['status'],
		"publish_date": request.form['publish-date'],
		"title": request.form['post-title'],
		"author": request.form['author'],
		"content": request.form['post-content'],
		"categories": request.form['categories'],
		"tag": request.form['tag'],
		# "lnk": request.form['link'],
		"last_update": str(DT.now(TZ.utc)),
		
	}
  
  try:
    sqlite_utils.Database('data_db/blog.sqlite3')['post'].update(post_id, upd_post_data, alter=True)
    flash("POST UPDATE SECCUESS")
  except sqlite3.OperationalError as e:
    flash(f"UPADTE ERROR: {e}")
  
  return redirect(url_for('blogger_mod', mod="blogger", pag="post_edit", title="POST UPDATE SUCCESS"))

def remove_post():
  post_id = request.args.get('id')
  
  try:
    sqlite_utils.Database('data_db/blog.sqlite3')['post'].delete(int(post_id))
    return jsonify({"DEL SUCCESS": "REMOVEED"})
  except sqlite3.OperationalError as e:
    return jsonify({"ERROR": f"ERROR: {e}"})
