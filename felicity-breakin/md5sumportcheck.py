import hashlib

for i in range (0,70000) :
    m = hashlib.md5()
    m.update(str(i).encode("utf-8"))
    if "c92841e00dbfeb12a0ce7fb3ffbd1fcb" == m.hexdigest() :
        print(i)
