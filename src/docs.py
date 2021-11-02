"""
commands to make documentation for: 
	ls
	mk
	rmd
	touch
	cat

"""

availableCommands = """
ls:
mk => mkdir
rmd => remove dir
touch => make files
cat => read files
Encoder => encode/decode (base64, base32....)
compiler => compiler c++/c files automatically
"""

cdDoc = """
Navigation command, it serves the purpose of changing the current dir
Usage: cd <pathtogoto>
example: cd /users/pc/user01
"""
touchDoc = """
touch ==> create files with one touch.
    Example:
        touch main.py ==> creates a file called main.py
        but if you want to make more than one file, then use this command
        touch main.py main.js main.c main.html ==> creates more than one file with the specified names
"""

ScrapDoc = """

a web tool similar to curl but you can specify anything you want to
grab from  a web page :)
usage: scrap <url> the boom magic!!

if you specify something like:
scrap <url> headers => prints the headers
scrap <url> text => prints the text 
scrap <url> json => prints the json
scrap <url> content => prints the content of the url including the html/javascript

"""


catDoc = """

cat ==> checking the content of a file.
Example:
cat main.py ==> displays the content of the main.py

and redirecting is possible:
	cat ex.py > ex2.py (redirects the content in append mode to ex2)
	cat ex.py >> ex2.py (redirects the content in overwrite mode to ex2)
"""

mkDoc = """
command to make dirs
usage: mk <dir path dir to make>
"""


mim = """
quiting symbol: /|/,
"""