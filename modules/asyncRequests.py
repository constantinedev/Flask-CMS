import re, io, os, sys, ast, ssl, csv, json, sqlite_utils, requests, asyncio, base64
from datetime import datetime as DT, timezone as TZ, timedelta as TD
import cloudscraper
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, HardwareType, SoftwareEngine

operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.UNIX.value, OperatingSystem.MAC.value]
hardware_types = [HardwareType.MOBILE.value, HardwareType.SERVER.value]
software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.SAFARI.value, SoftwareName.ANDROID.value]
software_engines = [SoftwareEngine.GECKO.value, SoftwareEngine.WEBKIT.value, SoftwareEngine.BLINK.value]
user_agent_rotator = UserAgent(software_names=software_names, software_engines=software_engines, hardware_types=hardware_types, operating_systems=operating_systems, limit=100)
user_agent = user_agent_rotator.get_random_user_agent()

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

def_headers = {
	'User-Agent': user_agent,
	'Content-Type': 'text/html',
}

async def gun_shell(url, method, type, headers, payload):
	if url == "" or url is None:
		return {"status": "Error", "response": "URL was empty!"}
	
	if headers == {} or headers is None:
		headers = def_headers
	else:
		headers = def_headers.update(headers)
  
	if payload == {} or payload is None:
		payload = {}
	if type == "nor":
		return await nor_req(url, method, type, headers, payload)
	if type == "tor":
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
