##################################################################################################################
##
##  Author : Pakshal Shahikant Jain 
##  Date : 09/05/2021
##  Program : Automated Scipt To Display Current Running Process Of Machine At Time Interval of 1 Min
##
##################################################################################################################
import os
import time
import psutil
from sys import *
import schedule

i = 0

def ProcessDisplay(FolderName = "Marvellous") :
    Data = [] 
    global i 

    if not os.path.exists(FolderName) :
        os.mkdir(FolderName)
    
    File_Path = os.path.join(FolderName,"Marvellous%s.txt"%i)
    i = i + 1
    fd = open(File_Path,"w")

    for proc in psutil.process_iter() :
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)

    for element in Data :
        fd.write("%s\n"% element)

def main() :
    print("--------------Marvellous Infosystems----------------------")
    print("Script Title :" + argv[0])
    arr = ProcessDisplay()

    if argv[1] == '-u' or argv[1] == '-U' :
        print("Usage : Application_Name Schedule_Time Directory_Name")
        exit()

    if argv[1] == '-h' or argv[1] == '-H' :
        print("Help : It is used to create log file of Running Processes")
        exit()
    
    schedule.every(int(argv[1])).minutes.do(ProcessDisplay)
    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    main()