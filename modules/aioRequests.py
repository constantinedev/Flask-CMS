import re, os, io, sys, ast, ssl, csv, json, sqlite_utils, asyncio, aiohttp
from aiohttp_socks import ProxyType,ProxyConnector, ChainProxyConnector
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.SAFARI.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MAC.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=200)
user_agent = user_agent_rotator.get_random_user_agent()

async def gun_shell(url, method, type, headers, payload):
  if url == "" or url is None:
    return {"status": "Error", "response": "URL was empty!"	}
  if headers=={} or headers is None:
    headers={"User-Agent":user_agent, "Content-Type": 'application/json'}
  if payload=={} or payload is None:
    payload={}

  if type=="nor":
    async with aiohttp.ClientSession() as session:
      return await bulletfire(session, url, method, type, headers, payload)
  elif type=="tor":
    connector = ProxyConnector.from_url("socks5://127.0.0.1:9050")
    async with aiohttp.ClientSession(connector=connector) as session:
      return await bulletfire(session, url, method, type, headers, payload)
     
async def bulletfire(session, url, method, type, headers, payload):
  if method == "GET":
    async with session.get(url, headers=headers, data=payload) as response:
      if response.status == 200:
        retData = {
          'status': response.status,
          'method': method,
          'type': type,
          'response': await response.text()
        }
        return retData
      else:
        retData = {
          'status': response.status,
          'method': method,
          'type': type,
          'response': ""
        }
        return retData
  elif method == "POST":
    async with session.post(url, headers=headers, data=payload) as response:
      if response.status == 200:
        retData = {
          'status': response.status,
          'method': method,
          'type': type,
          'response': await response.text()
        }
        return retData
      else:
        retData = {
          'status': response.status,
          'method': method,
          'type': type,
          'response': ""
        }
        return retData
