from All_imports import *

k = 0
start = time.time()

def Duplicate(duplicate,FolderName = 'Marvellous'):
    global k 
    global start

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

    end = time.time()
    Time = end - start
    fd.write("\nTime Taken BY Program is : %f sec :"%Time)

    EMAIL_ADDRESS = # Your Mail ID
    EMAIL_PASSWORD = #Your Email Password
    sentTo =  'thechainsmokers78@gmail.com'
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
