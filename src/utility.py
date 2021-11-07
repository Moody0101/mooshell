from os import path
import requests
from requests import get


def dumptofile(filename, content):
	if path.exists(filename):
		with open(filename, 'a') as f:
			try:
				if isinstance(content, bytes):
					f.write(content.decode())
				elif isinstance(res.headers, requests.structures.CaseInsensitiveDict):
					f.write(str(content))
				else:
					f.write(content)

			except:
				f.write(str(content))
	else:
		with open(filename, 'w+') as f:
			try:
				if isinstance(content, bytes):
					f.write(content.decode())
				elif isinstance(res.headers, requests.structures.CaseInsensitiveDict):
					f.write(str(content))
				else:
					f.write(content)
			except:
				f.write(str(content))
				


def getContent(url):
	return get(url).content
def getHeaders(url):
	return get(url).headers
def getJson(url):
	return get(url).json
def getText(url):
	return get(url).text
def getEncoding(url):
	return get(url).encoding
