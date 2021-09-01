################################################################################################
##
##  Author : Pakshal Jain
##  Date : 25/05/2021
##  Program : Automation script which accept directory name and file extension from user 
##            And Renames all files with first file extension with the second file extention.                                          
##
###############################################################################################
import os 

def Rename(path,extension,extension2) :
    
    for Folder,SubFolder,Filename in os.walk(path) :
        for file in Filename :
            file_extension = os.path.splitext(file)[-1].lower()
            f = os.path.splitext(file)[0].lower()
            #File = os.path.splitext(file)[0]

            if file_extension == ".txt" :
                os.rename(file,f + extension2) 

            #print(file)

def main() :
    print("Jay Ganesh.........")

    print("Enter Folder Name You Want To Travel")
    path = input()

    print("Enter Extension You Want To Search")
    extension = input()

    print("Enter Extension You Want To Rename with")
    extension2 = input()

    Rename(path,extension,extension2)

if __name__ == "__main__" :
    main()