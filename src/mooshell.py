

"""
sys funcs/classes that I might use => stdin, stdout, stderr, platform, path, argv
os ... => rmdir, chdir, mkdir, getcwd, path, scandir, removedirs, 
remove, rename, stat_result, system, walk
shutil ... => disk_usage, move, copy, _make_zipfile
"""



from sys import (stdin, stdout, stderr, platform, path, argv, exit)
from os import (rmdir, chdir, mkdir, getcwd, path, scandir, removedirs, 
remove, rename, stat_result, system, walk)
from shutil import disk_usage, move, copy, _make_zipfile
from colorama import Fore
from time import sleep
from subprocess import check_output
from docs import *
from requests import get


DOC = f"""{Fore.YELLOW} 
---------------------------------
Commands: 
    mkdir : make dir
    touch : make file
    cd : navigate
    ls : list file/dirs
    rmdir : remove a dir
    cat : check the content of a file
    quit/exit : exits.
   {Fore.BLUE} Note : {Fore.YELLOW} you can run:
    commandName --help
    for more information 
----------------------------------
{Fore.WHITE} language: {Fore.BLUE} Python 3.9  
"""


class mooshell:

    def __init__(self):
        print(DOC)
        self.PRIMARY = Fore.BLUE
        self.SECANDARY = Fore.WHITE
        self.YELLOW = Fore.YELLOW
        self.ERR = Fore.RED
        self.dir = getcwd()
        self.run = True
        while self.run:
            try:
                self.prompt = input(f'{self.ERR}[mooshell] {self.YELLOW} {self.dir} => ' + self.SECANDARY)
                self.processArgs()
            except Exception as e:
                print(e)
    def processArgs(self):
        if len(self.prompt.split(' ')) == 1:
            self.promp =  self.prompt.strip().upper()
            if self.promp == "LS" or self.promp == "DIR":
                self.ls()
            elif self.promp == "CD":
                print()
                print(self.dir)
                print()
            elif self.promp == "QUIT" or self.promp == "EXIT":
                self.quit()
            elif self.promp == "ENCODER":
                self.args = None
                self.Cmd()

            elif self.promp == "COMMANDS":
                print(availableCommands)
            elif self.promp == "SCRAP":
                print(ScrapDoc)
            else:
                self.args = None
                self.Cmd()
        elif len(self.prompt.split(' ')) > 1:
            if self.prompt.split(' ')[0].strip().upper() == "CD":
                self.changedir(self.prompt.split(' ')[1])
            elif self.prompt.split(' ')[0].strip().upper() == "TOUCH":
                if len(self.prompt.split(' ')) > 2:
                    self.touch(self.prompt.split(' ')[1:])
                else:
                    self.touch(self.prompt.split(' ')[1])
            elif self.prompt.split(' ')[0].strip().upper() == "MKDIR":
                if self.prompt.split(' ')[1].strip().upper() == '--help' or self.prompt.split(' ')[1].strip().upper() == '-h':
                    print(mkDoc)
                else:
                    try:
                        mkdir(self.prompt.split(' ')[1])
                    except:
                        print('something went wrong!!')
            elif self.prompt.split(' ')[0].strip().upper() == "RMDIR":
                try:
                    rmdir(self.prompt.split(' ')[1])
                except:
                    print('something went wrong!!')
            elif self.prompt.split(' ')[0].strip().upper() == "ENCODER":
                self.setArgs()
                self.Cmd()
            elif self.prompt.split(' ')[0].strip().upper() == "COMPILER":
                self.setArgs()
                self.Cmd()
            elif self.prompt.split(' ')[0].strip().upper() == "CAT":
                if self.prompt.split(' ')[1] == '--help' or self.prompt.split(' ')[1] == '-h':
                    print(catDoc)
                else:
                    self.cat()
            elif self.prompt.split(' ')[0].strip().upper() == "LS" or self.prompt.split(' ')[0].strip().upper() == "DIR":
                self.dir = self.prompt.split(' ')[1]
                self.ls()
            elif self.prompt.split(' ')[0].strip().upper() == "HELP":
                print()
                print(availableCommands)
                print()
            elif self.prompt.split(' ')[0].strip().upper() == "SCRAP":
                if len(self.prompt.split(' ')) == 2:
                    if self.prompt.split(' ')[1] == '--help' or self.prompt.split(' ')[1] == '-h':
                        print(ScrapDoc)
                    else:
                        self.scrap(self.prompt.split(' ')[1])
                elif len(self.prompt.split(' ')) == 3:
                    self.scrap(self.prompt.split(' ')[1], [self.prompt.split(' ')[2]])
            else:
                self.setArgs()
                self.Cmd()
    def setArgs(self):
       self.args = ' '.join(self.prompt.split(' ')[0:])
    def ls(self):
        print()
        for _ in scandir(self.dir):
                print(self.PRIMARY + '  [*]  ' + self.SECANDARY + _.name)
        print()
    def changedir(self, d):
        if d == '--help':
            print(cdDoc)
        else:
            if path.exists(d):
                chdir(d)
                self.dir = getcwd()
            else:
                print(f'{self.SECANDARY} it seems like it does not exist!')
    def touch(self, name):
        if name == '--help' or '-h':
            print(touchDoc)
        else:
            if isinstance(name, list):
                for _ in name:
                    self.touch(_)
            else:
                return open(name, 'w+').close()
    def scrap(self, url, args=[]):
        if len(args) == 0:
            if get(url).status_code == 200:
                res = {
                    0: get(url).content,
                    1: get(url).headers,
                    2: get(url).encoding,
                    3: get(url).json(),
                    4: get(url).text
                }
                print(f"{Fore.GREEN} status_code = 200 OK")
                scr = True
                while scr:
                    req = int(input(f"""
        {self.SECANDARY}
        specify what you want:
        (0) content
        (1) headers
        (2) Encoding
        (3) json
        (4) text
        (99) exit
        """))
                    print()
                    try:
                        if req in res.keys():
                            print(res[req])
                        else:
                            if req == 99:
                                scr = False
                            else:
                                print("the number you specified is wrong! try again")
                    except Exception as e:
                        print(e)
            else:
                print(f"{Fore.GREEN} status_code =  {get(url).status_code} :(")
        else:
            res = {
                'content': get(url).content,
                'headers': get(url).headers,
                'Encoding': get(url).encoding,
                'json': get(url).json(),
                'text': get(url).text
                }
            print(res[arg])
    def Cmd(self):
        try:
            if platform == "win32":
                if self.args is not None:
                    print(check_output(self.args).decode("utf-8"))
                else:
                    print(check_output(self.prompt.strip()).decode("utf-8"))
            else:
                if self.args is not None:
                    string = " ".join(self.args)
                    print(check_output(f"python3 {string}").decode("utf-8"))
                else:
                    print(check_output(self.prompt.strip()).decode("utf-8"))
        except Exception as e:
            print(e)
    def cat(self):
        if self.exist(self.prompt.split(' ')[1]):
            if len(self.prompt.split(' ')) > 2:
                if not self.exist(self.prompt.split(' ')[3]):
                    self.touch(self.prompt.split(' ')[3])
                if self.prompt.split(' ')[2] == ">>":
                    with open(self.prompt.split(' ')[1]) as f:
                        with open(self.prompt.split(' ')[3], 'w+') as f2:
                            f2.write(f.read())
                            print(f"{self.prompt.split(' ')[1]} > {self.prompt.split(' ')[3]}")
                            return
                elif self.prompt.split(' ')[2] == ">":
                    with open(self.prompt.split(' ')[1]) as f:
                        with open(self.prompt.split(' ')[3], 'a') as f2:
                            f2.write(f.read())
                            print(f"{self.prompt.split(' ')[1]} > {self.prompt.split(' ')[3]}")
                            return
            else:
                with open(self.prompt.split(' ')[1]) as f:
                    print(f.read())
        else:
            print(f"{self.ERR} this file you specified does not exist")

    def exist(self, p):
        return path.exists(p)
    def quit(self):
        print(' --- quiting --- ')
        sleep(1)
        self.run = False
def main():
    mooshell()
    print(Fore.WHITE)
main()