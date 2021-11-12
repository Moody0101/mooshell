
doc = """

GET functionality:

Database --login [dbName] [password] => consoles all the data in the db.
Database --login => will ask for dbName and paswword and outputs the db.
Database --getHeaders [dbName] [password] => gets and consoles all the headers
Database --getHeaders => gets and consoles all the headers (asks for name/password!)

Database --getItems [dbName] [password] => get the items.

POST functionality:

Database --register => to make new dataBase and password for it.
Database --register  [dbName] [password]=> to Make db more quickly.
Database --update [dbname] [password] [header] [data]

the header my name.

Database --help or -h => to get some help.

"""
from hashlib import sha256
from bases import base64
from os import getenv, path, mkdir, system, remove
from os import name as osS
from colorama import Fore
from sys import argv
from time import sleep
from json import dumps, loads
user = getenv("USERPROFILE") + "\\" + "data0101"



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
'WHITE', 'YELLOW'
]

YELLOW = Fore.YELLOW
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
WHITE = Fore.WHITE
CYAN = Fore.CYAN

def animation(Duration: int, string: str, COLOR=BLUE) -> None:
	for _ in ['\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-']:
		print(f"{COLOR} {string} {_}{WHITE}", end="\r")
		sleep(Duration)

class database:
	def __init__(self, dbPATH=user, dbName=None, password=None, data=None):
		self.dbPATH = dbPATH
		self.dbName = dbName
		self.abs = f"{self.dbPATH}\\{self.dbName}.json"
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
	def POST(self, ELEMENTS: tuple):
		"""
	you post a tuple because you are going to have a header and also the data.

	for instance you want to post a PASSWORD or TOken in the db you are going to do this:
		
	Database [dbName] dataHeader=Token data=zsdhusqzyysbzsy

	or whatever then this method is going to be exectuted like this: DB.POST((dataHeader, data))

		"""
		self.OPEN()
		if isinstance(self.login(), tuple):
			print(f"{RED}db {self.dbName} does not exist!!{WHITE}")
		else:
			if self.login():
				data1 = self.GET
				data = self.getdata
				ELEMENTS[1] = base64(ELEMENTS[1])._encode()
				data.append(ELEMENTS)
				data1.update({"data": data})
				with open(self.abs, "w+") as f:
					f.write(dumps(data1))
					print(f'{GREEN} db updated successfully! {GREEN}')
			else:
				print(f"{RED} incorrect Password!{WHITE}")
	@property
	def GET(self):
		with open(self.abs, 'r') as f:
			data = loads(f.read())
		return data
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
					for _ in self.getdata:
						print(f"{BLUE}[*] {YELLOW}{_[0]}:\n")
						print()
				else:
					print(f"{self.dbName} is an Empty database")
			else:
				print(f"{RED} incorrect Password!{WHITE}")
	def login(self):
		if path.exists(self.abs):
			if self.getpassword == sha256(self.password.encode()).hexdigest():
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
					print(f"{YELLOW} dataBase Name => {CYAN} {self.dbName}")
					print(f"{YELLOW} password hash => {CYAN} {self.getpassword}")

					print()
					for _ in self.getdata:

						print(f"{BLUE}[*] {GREEN}{_[0]}:\n\t{YELLOW}{base64(str(_[1]))._decode()}{WHITE}\n")
						print()
				else:
					print(f"{self.dbName} is an Empty database")
			else:
				print(f"{RED} incorrect Password!{WHITE}")
	def creatpassWord(self, p=None):
		if not p:
			password = input("Enter password: ").strip()
			password0 = input("Confirm: ").strip()
			while password != password0:
				print({Fore.RED} + "Not identical, try again")
				password = input("Enter password: ").strip()
				password0 = input("Confirm: ").strip()
		else:
			password = p
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

	def register(self, psswd=None):
		if not self.dbexists():
			password = self.creatpassWord(p=psswd)

			data = dumps({"password":f"{password}","data":[]}, indent=4)
			print(data)
			with open(self.abs, 'w+') as f:
				f.write(data)
			print(f"{GREEN} Database {self.dbName} was cereated successfully!!{WHITE}")
			print('password is : ', password)
			print(doc)
			return 1
		else:
			ch = input(f"{RED} db {self.dbName} does exist wanna delete (yes/no) {WHITE}")
			if ch.upper().strip() in ["YES", "Y"]:
				remove(self.abs)
				self.register()
			else:
				pass
	def cleardb(self):
		self.OPEN()
		if isinstance(self.login(), tuple):
			print(f"{RED} db {self.dbName} does not exist!!{WHITE}")
		else:
			if self.login():
				data1 = self.GET
				
				data1.update({"data": []})
				with open(self.abs, "w+") as f:
					f.write(dumps(data1))
					animation(0.4, "cleaning the database.", RED)
					print(f'{GREEN} db was cleaned successfully! {GREEN}')
			else:
				print(f"{RED} incorrect Password!{WHITE}")
	def cleanUp(self):
		close = input(f"{CYAN}PRESS ANY KEY TO CLOSE!")
		for _ in ['.'*i for i in range(6)]:
			print(f"{CYAN}closing the db{_}{WHITE}", end='\r')
			sleep(0.4)
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
			elif argv[n+1] == "--update":
				dbname = input(f"{YELLOW}DbName: {WHITE}")
				dbpassword = input(f"{YELLOW}Password: {WHITE}")
				db.database(dbName=dbname, password=dbpassword)
				db.OPEN()
				print("Not availabe yet:")
				db.cleanUp()
			elif argv[n+1] == "--clear":
				dbname = input(f"{YELLOW}DbName: {WHITE}")
				dbpassword = input(f"{YELLOW}Password: {WHITE}")
				db.database(dbName=dbname, password=dbpassword)
				db.cleardb()
				db.cleanUp()
			else:
				print(doc)
	elif len(argv) > 2:
		if argv[1+n] == "--register":
			# cmd = arg0 --register dbName password  (make new db, with this name and passsword!)
			if len(argv) == 4+n:	
				animation(0.3,"initializing database!")
				print(f'{YELLOW}initialized!!{WHITE}')
				db = database(dbName=argv[2+n])
				db.register(psswd=argv[3+n])
				db.cleanUp()
				exit(0)
			else:
				print(f"{RED}either the database name of the password is messing!{WHITE}")
		elif argv[1+n] == "--login":
			if len(argv) == 4+n:
				#cmd2 = arg0 --login dbName password (login using this name and password!)
				print(f"{BLUE}Querying the database..{WHITE}")
				sleep(2)
				db = database(dbName=argv[2+n], password=argv[3+n])
				db.QueryDb()
				db.cleanUp()
			else:
				print(f"{RED}either the database name of the password is messing!{WHITE}")
		elif argv[1+n] == "--update":
			if len(argv) >= 5+n:
				db = database(dbName=argv[2+n], password=argv[3+n])
				db.POST([argv[4+n], argv[5+n]])
				db.cleanUp()
			else:
				print(len(argv))
				print(f"{RED}either the database name of the password is messing!{WHITE}")
		elif argv[1+n] == "--clear":
			if len(argv) >= 4+n:
				db = database(dbName=argv[2+n], password=argv[3+n])
				db.cleardb()
				db.cleanUp()
			else:
				print(len(argv))
				print(f"{RED}either the database name of the password is messing!{WHITE}")
	else:
		print(doc)

if __name__ == '__main__':
	execute()
