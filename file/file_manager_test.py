import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "/" + f       # 윈도우에서는 \\
        if os.path.isdir(fullpath):
            print("[" + fullpath + "]")
            dumpdir(fullpath)
        else:
            print("\t" + fullpath)

dumpdir("/Users/choicihwan/Documents")