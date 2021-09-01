##############################################################################################################
##
##  Author : Pakshal Shashikant Jain 
##  Date : 20/05/2021
##  Program : Automated Mail Sending Script With Removal of Duplicate Files using MD5 Checksum
##
##############################################################################################################
from sys import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os 
import time
import hashlib
import schedule

def CheckExits(DirectoryName) :
    duplicate = {}

    if not os.path.exists(DirectoryName) :
        print("Directory Not Found..")
        exit()
    else :
        duplicate = DirectoryTraversal(DirectoryName)
    
    Duplicate(duplicate)

def CalculateChecksum(path,blocksize = 1024) :
    fd = open(path,'rb')
    hobj = hashlib.md5()

    buffer = fd.read(blocksize)
    while len(buffer) > 0 :
        hobj.update(buffer)
        buffer = fd.read(blocksize)

    fd.close()
    return hobj.hexdigest()

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

k = 0

def Duplicate(duplicate,FolderName = 'Marvellous'):
    global k 

    output = list(filter(lambda x : len(x) > 1,duplicate.values()))

    if not os.path.exists(FolderName) :
        os.mkdir(FolderName)

    File_Path = os.path.join(FolderName,"Marvellous%d.txt"%k)
    k = k + 1

    fd = open(File_Path,'w')
    fd.write("------------------------------------Final Output of This Project------------------------------------\n")
    fd.write("\nDuplicate Files Names With There Directory Names are : %s\n"%output)

    icnt = 0
    i = 0
    j = 0

    fd.write("\nPath Deleted are : ")
    for result in output :
        icnt = 0
        for path in result :
            icnt += 1
            i += 1
            value = [] 
            if icnt >= 2 :
                fd.write("%s, "%path)
                j += 1
                os.remove(path)

    fd.write("\n\nTotal Numbers of Files in Entered Directory were : %d\n"%i)
    fd.write("\nNumber of Files After Deleteing Duplicate Files are : %d\n"%j)
    fd.write("\n---------------------Thank You For Using This Application Now You Can Check Your Directory--------------------")

    EMAIL_ADDRESS = #Your Email Account 
    EMAIL_PASSWORD = #Your Email Password
    sentTo =  #Email Account To Whom You Want To Send Mail
    subject = "Report Of Dupicate Files Deleted"
    message = "Hiiiiii"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = sentTo
    msg['Subject'] = subject

    filename = os.path.basename(File_Path)
    fd = open((File_Path),'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((fd).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= %s"%filename)

    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS,sentTo,text)
    server.quit()


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


    schedule.every(int(argv[2])).hour.do(CheckExits,argv[1])

    while True :
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__" :
    main()