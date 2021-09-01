from All_imports import *

def CalculateChecksum(path,blocksize = 1024) :
    fd = open(path,'rb')
    hobj = hashlib.md5()

    buffer = fd.read(blocksize)
    while len(buffer) > 0 :
        hobj.update(buffer)
        buffer = fd.read(blocksize)

    fd.close()
    return hobj.hexdigest()
