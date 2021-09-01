#############################################################################################################################
##
##  Author : Pakshal Shashikant Jain 
##  Date : 25/05/2021
##  Program/Project : Script for Removal of Duplicate Files Using MD5 Checksum After Time Interval of 1 minute
##
##############################################################################################################################
from All_imports import *
from CheckExists import *

def main() :
    if(len(argv) != 3) :
        print("Error : Invalid Number of Arguments")
        exit()
    
    if (argv[1] == '-h') or (argv[1] == '-H') :
        print("It is Directory Cleaner Script")
        exit()

    if(argv[1] == "-u") or (argv[1] == '-U') :
        print("Usage : Provide the Absolute path of the Target Directory")
        exit()


    schedule.every(int(argv[2])).minutes.do(CheckExits,argv[1])

    while True :
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__" :
    main()