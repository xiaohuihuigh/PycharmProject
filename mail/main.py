#coding=utf-8
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
import mimetypes
smtpserver = 'smtp.qiye.aliyun.com'

user = 'zhaoyinghui@afa.ai'
password = 'aA950426'
sender = user
receiver= user
message = MIMEMultipart()
message['From'] = Header(sender,'utf-8')
message['To'] = Header(sender,'utf-8')
message['Subject'] = Header('ab','utf-8')

filename = '/home/zyh/tidb-docker-compose1.tar.gz01'
data = open(filename,'rb')
ctype,encoding = mimetypes.guess_type(filename)
if ctype is None or encoding is not None:
    ctype = 'application/octet-steam'
maintype,subtype = ctype.split('/',1)
print maintype,subtype
file_msg = MIMEBase(maintype,subtype)
file_msg.set_payload(data.read())
data.close()
file_msg.add_header('Content-disposition','attachment',filename=os.path.basename(filename))
message.attach(file_msg)

filename = '/home/zyh/tidb-docker-compose1.tar.gz00'
data = open(filename,'rb')
ctype,encoding = mimetypes.guess_type(filename)
if ctype is None or encoding is not None:
    ctype = 'application/octet-steam'
maintype,subtype = ctype.split('/',1)
print maintype,subtype
file_msg = MIMEBase(maintype,subtype)
file_msg.set_payload(data.read())
data.close()
file_msg.add_header('Content-disposition','attachment',filename=os.path.basename(filename))
message.attach(file_msg)


smtp = smtplib.SMTP()
smtp.connect(smtpserver,25)
smtp.login(user,password)
smtp.sendmail(sender,receiver,message.as_string())
smtp.quit()
