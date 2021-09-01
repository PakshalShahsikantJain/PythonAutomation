from All_imports import *
from DirectoryTraversal import *
from Duplicate import *

def CheckExits(DirectoryName) :
    duplicate = {}

    if not os.path.exists(DirectoryName) :
        print("Directory Not Found..")
        exit()
    else :
        duplicate = DirectoryTraversal(DirectoryName)
    
    Duplicate(duplicate)
