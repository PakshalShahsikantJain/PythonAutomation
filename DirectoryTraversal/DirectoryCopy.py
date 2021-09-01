###################################################################################################################################
##
##  Author : Pakshal Shahikant Jain 
##  Date : 25/05/2021 
##  Program : Automation script which accept two directory names and Copies all files from first directory into second directory.
##
###################################################################################################################################

import os 
import shutil

def DirectoryCopy(path,path2) :

    for Folder,SubFolder,Filename in os.walk(path) :
        for File in Filename :
            if not os.path.exists(path2) :
                os.mkdir(path2)
            else :
                shutil.move(path +'/'+File,path2+'/'+ File)

def main() :
    print("Jay Ganesh.........")
    print("Enter Directory Name You Want To Travel")
    path = input()

    print("Enter Directory Name You Want To Copy Strings into")
    path2 = input()

    DirectoryCopy(path,path2)

if __name__ == "__main__" :
    main()