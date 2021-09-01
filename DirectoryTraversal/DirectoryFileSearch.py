########################################################################################
##
##  Author : Pakshal Jain
##  Date : 25/05/2021
##  Program : Automation script which accept directory name and file extension from user 
##            And Display all files with that extension.                                          
##
########################################################################################
import os 

def Display(path,extension) :
    print("File Names With Same Extesions are : ")
    for Folder,SubFolder,Filename in os.walk(path) :
        for file in Filename :
            file_extension = os.path.splitext(file)[-1].lower()

            if file_extension == extension :
                print(file)

def main() :
    print("Jay Ganesh..........")
    
    print("Enter Directory You Want To Travel")
    Path = input()

    print("Enter Extension You Want To Search For")
    Extension = input()

    Display(Path,Extension)

if __name__ == "__main__" :
    main()
