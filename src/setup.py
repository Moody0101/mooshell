from os import system

MODULES = [
"colorama",
"requests",
"pafy",
"youtube-dl"
]


for i in MODULES:
	try:
		system(f"pip install {i}")
	except:
		print("something went wrong!")
