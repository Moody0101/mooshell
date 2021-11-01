
from base64 import (b64encode, b64decode, b32encode, b32decode, b16encode, b16decode, b85encode, b85decode)
from os import path
from sys import argv, exit

class Encoder:
    """
    I am making a base hasher, cuz windows lacks that.
    algorithms: b64encoden, b32encode, b16encode, b85encode
    """
    def __init__(self):
        self.file = None
        self.string = None
        self.EncodeFile = False
        self.available = {
        "BASE64": [b64encode, b64decode],
        "BASE32": [b32encode, b32decode],
        "BASE16": [b16encode, b16decode],
        "BASE85": [b85encode, b85decode]
        }
        self.e, self.d = 0, 1
        try:
            self.setUp()
        except:
            exit()

    def setUp(self):

        if len(argv) == 1:
            print("""
    usage: Encode <text> --base [base] -e/-d --file 
    --base: base32 for example 
    --e: encode
    --d: decode
    --file: adding the flag makes <text> a fileName that has the text to be processed
        """)
            exit()
        elif len(argv) == 2 or len(argv) == 3:
            if '--help' in argv:
                print("""
        usage: Encode <text> --base [base] -e/-d --file 
        --base: base32 for example 
        --e: encode
        --d: decode
        --file: adding the flag makes <text> a fileName that has the text to be processed
            """)
            print("the base is not specified! try: Encoding <text> --base base64")
            exit()
        elif len(argv) == 4: 
            if str(argv[3]).upper().strip() not in list(self.available.keys()):
                print(f"{argv[3]} is not available")
                exit()
            else:
                self.string = argv[1]
                self.algo = self.available[str(argv[3]).upper().strip()]
                self.encoding = ""
        elif len(argv) >= 5:
            if argv[4] not in ["-e", "-d"]:
                print("something went wrong")
                print("""
    usage: Encode <text> --base [base] -e/-d --file [fileName]
    --base: base32 for example 
    --e: encode
    --d: decode
        """)
                exit()
            else:
                self.string = argv[1]
                self.algo = self.available[str(argv[3]).upper().strip()]
                self.encoding = argv[4]
                try:
                    if argv[5] == "--file":
                        self.EncodeFile = True
                    else:
                        self.EncodeFile = False
                except:
                    pass
        self.hash()
    def hash(self):
        if self.EncodeFile:
            if not path.exists(self.string):
                print(f"this file => {self.string} does not exist")
                exit()
            with open(self.string) as f:
                print("Working on processing...")
                text = f.read().encode()
                if self.encoding == "-e":
                    print(self.algo[self.e](text).decode("utf-8"))
                elif self.encoding == "-d":
                    print(self.algo[self.d](text).decode("utf-8"))
                
        else:
            if self.encoding == "-e":
                print(self.algo[self.e](self.string.encode()).decode("utf-8"))
            elif self.encoding == "-d":
                print(self.algo[self.d](self.string.encode()).decode("utf-8"))
            else:
                print(self.algo[self.e](self.string.encode()).decode("utf-8"))

if __name__ == '__main__':
    en = Encoder()

