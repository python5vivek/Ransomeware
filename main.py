from cryptography.fernet import Fernet
import os,sys

files = os.listdir()
target_files = []
for file in files:
    if file != "-_-.key" and file != "main.py":
        target_files.append(file)

fernet = Fernet(open("-_-.key","rb").read())

if len(sys.argv) != 2:
    print("Usage: python main.py <encode/decode>")
    sys.exit()

if sys.argv[1] == "encode":
    for tf in target_files:
        d = fernet.encrypt(open(tf,"rb").read())
        _1 = open(tf,"wb")
        _1.write(d)
        _1.close()
elif sys.argv[1] == "decode":
    for tf in target_files:
        d = fernet.decrypt(open(tf,"rb").read())
        _1 = open(tf,"wb")
        _1.write(d)
        _1.close()