from sys import argv
from time import sleep
from os import system, path


v: str = 'moo: 0.0.1'
compilecDoc: str = """

compile ==> a loop compiling a c++/c script every 5s.
    example:
    compile <compiler> <fileName>
    for c: compile gcc <fileName>
    for c++: compile g++ <fileName>

additional Note: if the name of the file is Hello.c or hello.cpp,
it will compile it into a hello.exe anyways.
"""

class compile:

    def __init__(self, fileName: str=None):
        self.fileName = fileName
        self.validExt = ["cpp", "c"]
        self.compilers = ["gcc -o", "g++ -o"]
    def comp(self):
        co = path.isfile(self.fileName)
        dot = '.'
        if self.ext == "cpp":
            while co:
                system(
                        f"{self.compilers[1]} {self.fileName.split('.')[0]} {self.fileName}"
                        )
                print(f"compiling to {self.fileNam.split('.')[0]} you can edit now{dot}", end='\r')
                if len(dot) <= 3:
                    dot += '.'
                elif len(dot) > 3:
                    dot = '.'
                sleep(10)
            else:
                 print(f'the file {self.fileName} does not exist')
        else:
            while co:
                system(
                            f"{self.compilers[0]} {self.fileName.split('.')[0]} {self.fileName}"
                     )
                print(f"compiling to {self.fileName.split('.')[0]} you can edit now{dot}", end='\r')
                if len(dot) <= 3:
                    dot += '.'
                elif len(dot) > 3:
                    dot = '.'
                sleep(0.5)
            else:
                print(f'the file {self.fileName} does not exist')
    def checkExt(self):
        self.ext = self.fileName.split('.')[1]
        if self.ext not in self.validExt:
            print("invalid extention: compiling cpp, c files only")
            exit()
        else:
            self.comp()

    def execute(self):
        if len(argv) > 2 or len(argv) == 1:
            print("Invalid syntax: compile <fileName>")
        elif len(argv) == 2:
            if argv[1] == "--help" or argv[1] == "-h":
                print(compilecDoc)
            elif argv[1] == "--version" or argv[1] == "-v":
                print(v)
            else:
                self.fileName = argv[1]
                self.checkExt()


def main():

    compiler = compile()
    compiler.execute()


if __name__ == '__main__':
    main()

