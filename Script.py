########################################################################################################
##
##  Author : Pakshal Shahikant Jain 
##  Date : 09/05/2021
##  Program : Python Automated Script To Send Mail's (Mail Account Service Used "Gmail") 
##
########################################################################################################
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import psutil
from sys import *
import schedule

i = 0

def SendEmail(FolderName = "Marvellous") :
    email = #YouEmail address
    password = #YourEmail Password 
    sentTo =  #Email Address To Whom You Want To Send
    subject = "This is Demo Mail"
    message = "Hiiiiii"
    Data = [] 
    global i 

    if not os.path.exists(FolderName) :
        os.mkdir(FolderName)
    
    File_Path = os.path.join(FolderName,"Marvellous%s.txt"%i)
    i = i + 1
    for proc in psutil.process_iter() :
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)

    attachment = open(File_Path,"w")

    for element in Data :
        attachment.write("%s\n"%element)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sentTo
    msg['Subject'] = subject

    filename = os.path.basename(File_Path)
    attachment = open((File_Path),'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= %s"%filename)

    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(email,password)
    text = msg.as_string()
    server.sendmail(email,sentTo,text)
    server.quit()

def main() :
    print("--------------Marvellous Infosystems----------------------")
    print("Script Title :" + argv[0])
    arr = SendEmail()

    if argv[1] == '-u' or argv[1] == '-U' :
        print("Usage : Application_Name Schedule_Time Directory_Name")
        exit()

    if argv[1] == '-h' or argv[1] == '-H' :
        print("Help : It is used to create log file of Running Processes")
        exit()
    
    schedule.every(int(argv[1])).minutes.do(SendEmail)
    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    main()