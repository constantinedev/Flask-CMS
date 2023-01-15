import re, io, sys, json, sqlite_utils, requests
from datetime import datetime as DT, timezone as TZ
from flask_login import UserMixin, LoginManager

class setup_db:
  sqlite_utils.Database('db/admin.session')["agents"].create({
    "id": int,
    'type': str,
    'login_id': str,
    'pwd': str,
    "username": str,
    'email': str,
    'fname': str,
    'lname': str,
    'last_login': str,
    'last_update': str,
  },
    not_null=('login_id', 'pwd', 'email', 'username'),
    pk="id",
    if_not_exists=True
  )

  sqlite_utils.Database('db/admin.session').create_view('vlogin', f"SELECT id, login_id, username, email, fname, lname FROM agents;", replace=True)
  
  ### Blogger DB
  sqlite_utils.Database('data_db/blog.sqlite3')['post'].create({
    "id": int,
    "status": str,
    "publish_date": str,
    "title": str,
    "author": str,
    "content": str,
    "categories": str,
    "tag": str,
    "link": str,
    "crt_agent": str,
    "crt_date": str,
    "last_update": str,
  },
    pk="id",
    not_null=('id', 'author', 'title', 'content'),
    if_not_exists=True
  )
  
  sqlite_utils.Database('data_db/blog.sqlite3')['categories'].create({
    "id": int,
    "name": str,
    "link": str,
    "count": str,
    "description": str,
  },
    pk="id",
    not_null=('id', 'name', 'link'),
    if_not_exists=True
  )
  
  sqlite_utils.Database('data_db/blog.sqlite3')['categories'].create_index(["link", "name"], unique=True, if_not_exists=True)
  
  sqlite_utils.Database('data_db/blog.sqlite3')['tag'].create({
    "id": int,
    "count": str,
    "description": str,
    "link": str,
    "name": str,
  },
    pk="id",
    not_null=('id', 'name'),
    if_not_exists=True
  )

class agent(UserMixin):  
  def is_active(self):
    return True
  
  def is_authenticated(self):
    return self.is_active
  
  def is_anonymous(self):
        return False
  
  def get_id(self):
    try:
      return str(self.id)
    except AttributeError:
      raise NotImplementedError('No ID Find in system.`') from None
  
login = LoginManager()

@login.user_loader
def load_user(login_id):
  user_tok = agent()
  for row in sqlite_utils.Database('db/admin.session')['agents'].rows_where("login_id = :login_id", {"login_id": login_id}):
    user_tok.id = row['id']
    user_tok.login_id = row['login_id']
    user_tok.dpName = row['username']
    user_tok.email = row['email']
    user_tok.fname = row['fname']
    user_tok.lname = row['lname']
    
    # sqlite_utils.Database('db/admin.session')['agents'].update(int(row['id']), {"last_login": str(DT.now(TZ.utc))}, alter=True)
    return user_tok
