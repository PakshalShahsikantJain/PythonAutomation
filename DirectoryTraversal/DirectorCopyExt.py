###################################################################################################################################
##
##  Author : Pakshal Shahikant Jain 
##  Date : 25/05/2021 
##  Program : Automation script which accept two directory names and one file extension and Copies all
##            files with the specified extension from first directory into second directory.
##
###################################################################################################################################

import os 
from shutil import move 

def CopyFilesExt(path,path2,extension) :
    for Folder,SubFolder,Filename in os.walk(path) :
        for file in Filename :
            file_Extension = os.path.splitext(file)[-1].lower()
            
            if not os.path.exists(path2) :
                os.mkdir(path2)

            if file_Extension == extension :
                move(path +'/'+file,path2+'/'+file)

def main() :
    print("Jay Ganesh...........")
    print("Enter Directory Name")
    path = input()

    print("Enter Directory Name You Want To Copy Contents into")
    path2 = input()

    print("Enter Extension You Want To Copy")
    extension = input()

    CopyFilesExt(path,path2,extension)

if __name__ == "__main__" :
    main()