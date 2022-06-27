import csv
import os
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import email
from email import encoders
from glob import glob
from maling_parameter import footer,sever,FROM
def mail_reporting(subject,html_final,file,receiver):
    global all_filesnames
    html_final=html_final
    massage=MIMEMultipart("alternative",None)
    print("file",file)
    if file =="":
        print("No file attached")
    else:
        all_filesnames=glob(os.path.join(file,"*csv"))
        for a_file in all_filesnames:
            with open(a_file) as f:
                print("afile",a_file)
                reader=csv.reader(f)
                data=list(reader)
            if len(data)==1:
                print("Empty File")
            else:
                attachment=open(a_file,'rb')
                file_name=os.path.basename(a_file)
                part=MIMEBase("application","octet-stream")
                part.set_poyload(attachment.read())
                part.add_headder('Conternt-Disposition','Attachment',file_name=file_name)
                encoders.encode-base64(part)
                massage.attach(part)
    message['Subject']=subject
    msg1=MIMEText(html_final+footer,"html")
    massage.attach(msg1)
    mail.starttls()
    mail.ealo()
    mail.login(user=username,password=pwd)
    email.sendmail(FROM,receiver,message.as_string())
    mail.quit()
    print("Mail Sent")

