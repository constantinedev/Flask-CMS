import re, os, io, sys, ast, ssl, csv, json, requests, sqlite_utils
from datetime import datetime as DT, timezone as TZ, timedelta as TD

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

async def gun_shell(url, method, type, headers, payload):
	if url=="" or url is None:
		return {"status": "Error", "response": "URL was empty!"}
	if headers=={} or headers is None:
		headers={"Content-Type": 'application/json'}
	if payload=={} or payload is None:
		payload = {}
	if type=="nor":
		return await nor_req(url, method, type, headers, payload)
	if type=="tor":
		return await tor_req(url, method, type, headers, payload)

async def nor_req(url, method, type, headers, payload):
	if method == "GET":
		req = requests.get(url, headers=headers, data=payload)
	elif method == "POST":
		req = requests.post(url, headers=headers, data=payload)
	if req.status_code == 200:
		retData = {
			"status": req.status_code,
			'method': method,
			'type': type,
			"response": req.text
		}
		return retData
	else:
		retData = {
			"status": req.status_code,
			'method': method,
			'type': type,
			'response': ""
		}
		return retData

async def tor_req(url, method, type, headers, payload):
	if method == "GET":
		req = session.get(url, headers=headers, data=payload)
	elif method == "POST":
		req = session.post(url, headers=headers, data=payload)
	if req.status_code == 200:
		retData = {
			"status": req.status_code,
			'method': method,
			'type': type,
			"response": req.text
		}
		return retData
	else:
		retData = {
			"status": req.status_code,
			'method': method,
			'type': type,
			'response': ""
		}
		return retData