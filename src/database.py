"""
prototype => I will make a system to login, a system to post and get data.

data sample:

data = {
	'password': '185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969',
	'data': []
}
==> after checking the password we would just try to display the keys of the db
Usage: 

Flags: --signin, --login, --fetchdb, --help, --getData

"""

from hashlib import sha256
from os import getenv, path, mkdir, system, remove
from colorama import Fore
from sys import argv
user = getenv("USERPROFILE") + "//" + "data0101"
if not path.exists(user):
	mkdir(user)

class database:
	def __init__(self, dbPATH=user, dbName, password, data):
		self.dbName = dbName
		self.abs = f"{self.dbPATH}{self.dbName}"
		self.password = password
		self.data = data
		self.OPEN()
		self.execute()
	@property
	def getpassword(self):
		"""
		gets the hashed password using the GET base command.
		"""
		return self.GET["password"]
	@property
	def getdata(self):
		"""
		gets all the data using the GET base command.
		"""
		return self.GET["data"]
	@property
	def getHeaders(self):
		"""
		gets all the headers...
		"""
		return [i[0] for i in self.getdata]
	@property
	def Gethint(self):
		return self.GET["Hint"]
	def POST(self, ELEMENTS: tuple):
		data = self.getdata
		data.append(ELEMENTS)
		data0 = self.GET().update("data": data)
		with open(self.abs) as f:
			f.write(dumps(data0))
			print('db updated successfully!')
	def GET(self):
		with open(self.abs, 'r') as f:
			data = loads(f.read())
		return data
	def OPEN(self):
		SetDbattrib('-H')
	def CLOSE(self):
		SetDbattrib('+H')
	def SetDbattrib(self, attr: str) -> bool:
		if os.exists(self.dbPATH):
			return False
		system(f"{self.abs} attrib {attr}")
		return True
	def login(self):
		if path.exists(self.abs):
			p = input("Enter password")
			if getpassword(self.abs)["password"] == sha256(p.encode()).hexdigest().decode():
				return True
			else:
				return (False, self.Gethint)
	def dbexists(self):
		return path.exists(self.abs)
	def makeDb(self):
		if not self.dbexists():
			data = dumps({"password":f"{sha256(password.encode()).hexdigest()}","data":[]}, indent=4)
			with open(self.abs, 'w+') as f:
				f.write(data)
			return 1
		else:
			ch = input(f"{Fore.RED} db {self.dbName} does exist wanna delete (yes/no) {Fore.WHITE}")
			if ch.upper().strip() in ["YES", "Y"]:
				remove(self.abs)
				self.makeDb(self.dbName)
			else:
				exit()
	def cleanUp(self):
		for _ in ['.'*i for i in range(6)]:
			print(f"closing the db{_}", end='\r')
		self.CLOSE()


"""
a func that will hander the logins and managing data in the databases.

"""
def execute():
	if len(argv) == 2 | len(argv) == 1:
		if len(argv) == 1 | argv[1] == '--help':
			print('doc')
		elif argv[1] == '--version':
			print('0.0.0!')
		else:
			print('doc')
	elif len(argv) > 2:
			pass