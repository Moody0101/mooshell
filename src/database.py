"""
prototype => I will make a system to login, a system to post and get data.

data sample:

data = {
	'password': '185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969',
	'data': []
}
==> after checking the password we would just try to display the keys of the db
Usage: 

Flags: --register, --login, --help

"""

doc = """
GET functionality:
Database --login => will ask for dbName and paswword and outputs the db.
Database --login [dbName] [password] => consoles all the data in the db.
Database --getHeaders [dbName] [password] => gets and consoles all the headers
Database --getItems [dbName] [password] => get the items.

POST functionality:
Database --register => to make new dataBase and password for it.
Database --register [password] [dbName] => to Make db more quickly.
Database --postData [password] [dbName] header=Myname data=Hossin => it posts the data with
the header my name.

Database --help or -h => to get some help.
"""
from hashlib import sha256
from os import getenv, path, mkdir, system, remove
from os import name as osS
from colorama import Fore
from sys import argv
from time import sleep
from json import dumps, loads
user = getenv("USERPROFILE") + "//" + "data0101"
if not path.exists(user):
	mkdir(user)

AvailableColors = [
'BLACK', 'BLUE',
'CYAN', 'GREEN',
'LIGHTBLACK_EX', 
'LIGHTBLUE_EX', 'LIGHTCYAN_EX',
'LIGHTGREEN_EX', 
'LIGHTMAGENTA_EX',
'LIGHTRED_EX', 'LIGHTWHITE_EX', 
'LIGHTYELLOW_EX', 'MAGENTA', 
'RED', 'RESET', 
'WHITE', 'YELLOW']

YELLOW = Fore.YELLOW
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
WHITE = Fore.WHITE

class database:
	def __init__(self, dbPATH=user, dbName=None, password=None, data=None):
		self.dbPATH = dbPATH
		self.dbName = dbName
		self.abs = f"{self.dbPATH}{self.dbName}"
		self.password = password
		self.data = data

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
	
	def POST(self, ELEMENTS: tuple):
		"""
	you post a tuple because you are going to have a header and also the data.

	for instance you want to post a PASSWORD or TOken in the db you are going to do this:
		
	Database [dbName] dataHeader=Token data=zsdhusqzyysbzsy

	or whatever then this method is going to be exectuted like this: DB.POST((dataHeader, data))

		"""
		data = self.getdata
		data.append(ELEMENTS)
		data0 = self.GET().update({"data": data})
		with open(self.abs) as f:
			f.write(dumps(data0))
			print('db updated successfully!')
	def GET(self):
		with open(self.abs, 'r') as f:
			data = loads(f.read())
		return 
	def SetDbattrib(self, attr: str) -> bool:
		if path.exists(self.dbPATH):
			return False
		system(f"{self.abs} attrib {attr}")
		return True
	def OPEN(self):
		self.SetDbattrib('-H')
	def CLOSE(self):
		self.SetDbattrib('+H')
	
	def getHeaders(self):
		"""
		gets all the headers...
		"""
		self.OPEN()
		if isinstance(self.login(), tuple):
			print(f"{RED}db {self.dbName} does not exist!!{WHITE}")
		else:
			if self.login():
				if len(self.getdata) >= 1:
					print(f"{self.dbName} headers:")
					for _ in self.getdata():
						print(f"{BLUE}[*] {YELLOW}{_[0]}:\n")
						print()
				else:
					print(f"{self.dbName}Empty database")
			else:
				print(f"{RED} incorrect Password!{WHITE}")
	def login(self):
		if path.exists(self.abs):
			if getpassword(self.abs) == sha256(self.password.encode()).hexdigest().decode():
				return True
			else:
				return False
		return (False,False)
	def dbexists(self):
		return path.exists(self.abs)
	def QueryDb(self):
		self.OPEN()
		if isinstance(self.login(), tuple):
			print(f"{RED}db {self.dbName} does not exist!!{WHITE}")
		else:
			if self.login():
				if len(self.getdata) >= 1:
					print(f"[@] db Name {self.dbName}")
					for _ in self.getdata():

						print(f"{BLUE}[*] {GREEN}{_[0]}:\n{YELLOW}{_[1]}{YELLOW}\n")
						print()
				else:
					print(f"{self.dbName}Empty database")
			else:
				print(f"{RED} incorrect Password!{WHITE}")
	def creatpassWord(self):
		password = input("Enter password: ").strip()
		password0 = input("Confirm: ").strip()
		while password != password0:
			print({Fore.RED} + "Not identical, try again")
			password = input("Enter password: ").strip()
			password0 = input("Confirm: ").strip()
		else:
			return sha256(password.encode()).hexdigest()
	def getItems(self):
		self.OPEN()
		if isinstance(self.login(), tuple):
			print(f"{RED}db {self.dbName} does not exist!!{WHITE}")
		else:
			if self.login():
				print(f'{self.dbName} items')
				if len(self.getdata) >= 1:
					for _ in self.getdata():
						print(f"{_[1]}\n")
						print()
				else:
					print(f"{self.dbName}Empty database")
			else:
				print(f"{RED} incorrect Password!{WHITE}")

	def register(self):
		
		if not self.dbexists():
			password = self.creatpassWord()
			data = dumps({"password":f"{password}","data":[]}, indent=4)
			with open(self.abs, 'w+') as f:
				f.write(data)
			print(f"{GREEN} Database {self.dbName} was cereated successfully!!{WHITE}")
			print(doc)
			return 1
		else:
			ch = input(f"{RED} db {self.dbName} does exist wanna delete (yes/no) {WHITE}")
			if ch.upper().strip() in ["YES", "Y"]:
				remove(self.abs)
				self.register()
			else:
				exit()
	def cleanUp(self):
		for _ in ['.'*i for i in range(6)]:
			print(f"closing the db{_}", end='\r')
		self.CLOSE()


def execute():
	"""
	a func that will hander the logins and managing data in the databases.
	"""
	n = 0
	if osS != 'nt':
		n = 1
	if len(argv) == n+2 or len(argv) == n+1:
		if argv[n+1] == '--help':
			print(doc)
		elif argv[n+1] == '--version':
			print('0.0.0!')
		else:
			if argv[n+1] == "--register":
				dbname = input(f"{YELLOW}DbName: {WHITE}")
				
				for _ in ['\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-']:
					print(f"{BLUE} initializing database! {_}{WHITE}", end="\r")
					sleep(0.3)
				print(f'{YELLOW}initialized!!{WHITE}')
				db = database(dbName=dbname)
				db.register()
				db.cleanUp()
				exit(0)
			elif argv[n+1] == "--login":
				dbname = input(f"{YELLOW}DbName: {WHITE}")
				dbpassword = input(f"{YELLOW}Password: {WHITE}")
				print(f"{BLUE}Querying the database..{WHITE}")
				db = database(dbName=dbname, password=dbpassword)
				db.QueryDb()
				db.cleanUp()
			elif argv[n+1] == "--getItems":
				dbname = input(f"{YELLOW}DbName: {WHITE}")
				dbpassword = input(f"{YELLOW}Password: {WHITE}")
				print(f"{BLUE}Querying the database..{WHITE}")
				db = database(dbName=dbname, password=dbpassword)
				db.database(dbName=dbname, password=dbpassword)
				db.getItems()
				db.cleanUp()
			elif argv[n+1] == "--getHeaders":
				dbname = input(f"{YELLOW}DbName: {WHITE}")
				dbpassword = input(f"{YELLOW}Password: {WHITE}")
				print(f"{BLUE}Querying the database..{WHITE}")
				db = database(dbName=dbname, password=dbpassword)
				db.database(dbName=dbname, password=dbpassword)
				db.getHeaders()
				db.cleanUp()
			else:
				print("made it")

				print(doc)
	elif len(argv) > 2:
		print('hu')
	else:
		len(argv)
		print(doc)

execute()
