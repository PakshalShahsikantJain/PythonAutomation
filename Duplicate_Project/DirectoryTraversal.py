from All_imports import *
from CalculateChecksum import *

def DirectoryTraversal(path) :
    duplicate = {}      
    for Folder,SubFolder,Filename in os.walk(path) :
        for file in Filename :
            actualpath = os.path.join(Folder,file)
            hash = CalculateChecksum(actualpath)

            if hash in duplicate :            
                duplicate[hash].append(actualpath)
            else :                           
                duplicate[hash] = [actualpath]

    return duplicate
