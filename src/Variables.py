"""
DOCUMENTATIONS FOR THE COMMANDS IN MOOSHELL
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


scanDoc = """
scanning diractory for the specified ext:
Usage: scan extantion.
ex: scan .txt or scan .png
"""


mvDoc = """


moving a file/MultipleFiles into  a specified distination:


Usage: mv source:path(s)/fileName(s) distination:path/Name

exemple(OneFile): mv ./file.txt c:/users/pc/whatever
example (MultipleFiles): mv  ./file.txt ./file.py ./file.html c:/users/pc/whatever
and that will move ./file.txt ./file.py ./file.html to the specified destination
"""


mim = """
quiting symbol: /|/
"""



Rmdoc = """
Removin one or multiple files
Usage: rm fileName/files 
example: rm main.js main.css main.txt
"""

FontdownloaderDoc = """
Downloading font by one command.
usage: fontD FontName
apis => google fonts, dafont
"""

HELP = """

 - basic command (mkdir, rmdir, cp, mv, rm...)
 - scrap -> web scrapping tool 
 - mim -> Text editor, even if it is not finished yet, I have problems, but shortly will be solved.
 - Encoder -> a tool decode/Encode base32, base64, base85..
 - Compiler -> a c++/c continuous compiling automation loop, only specify the file then it will continuously compile ur script automatically.
 -  database -> A data base to store data, it uses encryption, also you can costumize it using Database.py.
 - Crypto ->  a tool to scrap crypto currency data from the yahoo  finance api
 - fontD -> a font downloader that uses google font api and dafont api to download fonts more more easily
 - ORG -> a command to organize a directory.
"""

ORGdoc = """

A tool to organize files in  a folder.
USAGE:
    path files: a.mp3, x.mp4, p.py
After usage:
    path folders:
        Audio:
            a.mp3
        videos: 
            x.mp3
        code:
            p.py

"""