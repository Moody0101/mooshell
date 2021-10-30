

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


DOC = f"""{Fore.YELLOW} 
Commands: 
    mk : make dir
    touch : make file
    cd : navigate
    ls : list file/dirs
    Encode : decode/encode text
    rmd : remove a dir
    quit/exit : exits.
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
            self.prompt = input(f'{self.ERR}[**mooshell**] {self.YELLOW} {self.dir} => ' + self.SECANDARY)

            if len(self.prompt.split(' ')) == 1:
                self.promp =  self.prompt.strip().upper()
                if self.promp == "LS":
                    self.ls()
                elif self.promp == "CD":
                    print(self.dir)
                elif self.promp == "QUIT" or self.promp == "EXIT":
                    self.quit()
                elif self.promp == "ENCODER":
                    self.args = self.promp
                    self.encoder()
                else:
                    self.commad()
            elif len(self.prompt.split(' ')) > 1:
                if self.prompt.split(' ')[0].strip().upper() == "CD":
                    self.changedir(self.prompt.split(' ')[1])
                elif self.prompt.split(' ')[0].strip().upper() == "TOUCH":
                    self.touch(self.prompt.split(' ')[1])
                elif self.prompt.split(' ')[0].strip().upper() == "MK":
                    try:
                        mkdir(self.prompt.split(' ')[1])
                    except:
                        print('something went wrong!!')
                elif self.prompt.split(' ')[0].strip().upper() == "RMD":
                    try:
                        rmdir(self.prompt.split(' ')[1])
                    except:
                        print('something went wrong!!')
                elif self.prompt.split(' ')[0].strip().upper() == "ENCODER":
                    self.args = ' '.join(self.prompt.split(' ')[0:]) 
                    self.encoder()
                else:
                    self.commad()
    def ls(self):
        for _ in scandir(self.dir):
            print(self.PRIMARY + '=> ' + self.SECANDARY + _.name)
    def changedir(self, d):
        if path.exists(d):
            chdir(d)
            self.dir = getcwd()
        else:
            print(f'{self.SECANDARY} it seems like it does not exist!')
    def touch(self, name):
        ext = name.split('.')[1]
        with open(name, 'w+') as f:
            print(f'made one file (1) with this extantion .{ext}')
    def encoder(self):
        chdir('./bin')
        print(check_output(self.args).decode("utf-8"))
        chdir(self.dir)
    def commad(self):
        try:
            check_output(self.prompt).decode("utf-8")
        except Exception as e:
            print(e)

    def quit(self):
        print(' --- quiting --- ')
        sleep(1)
        self.run = False
def main():
    mooshell()
    print(Fore.WHITE)
main()