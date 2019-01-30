#coding=utf-8
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import MIMEBase

from email.header import Header
import mimetypes
import platform
if platform.python_version() == '3':
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser
class MailConf(object):
    def __init__(self):

        conf = ConfigParser()
        conf.read('user_count.conf')
        self.email =  conf.get('user_info','email')
        self.password = conf.get('user_info','password')
        self.smtpserver = conf.get('user_info','smtpserver')
        self.port = conf.get('user_info','port')
        self.name = conf.get('user_info','name')
        self.smtp = smtplib.SMTP()
        if self.email == "":
            self.email = self.r_input('please input the email:')
            self.input_smtpserver()
            self.input_password()

        try:
            self.smtp.connect(self.smtpserver, self.port)
        except Exception as e:
            print (e)
            print('smtpserver error')
            self.input_smtpserver()
        try:
            self.smtp.login(self.email,self.password)
        except Exception as e:
            print(e)
            print('email or password error')
            self.input_password()
        self.save_conf()
    def save_conf(self):
        conf = ConfigParser()
        conf.read('user_count.conf')
        conf.set('user_info','email',self.email)
        conf.set('user_info', 'password', self.password)
        conf.set('user_info', 'name', self.name)
        conf.set('user_info', 'smtpserver', self.smtpserver)
        conf.set('user_info', 'port', self.port)
        with open('user_count.conf','w')as f:
            conf.write(f)
    def r_input(self,str):
        if platform.python_version() == '3':
            return input(str)
        else:
            return raw_input(str)
    def input_password(self):
        t = 3
        while t:
            t-=1
            self.password = self.r_input('please input the password:')
            if self.password == self.r_input('please input the password again:'):
                if self.smtpserver != "":
                    try:
                        self.smtp.login(self.email,self.password)
                    except Exception as e:
                        print e
                    else:
                        break
            else:
                print("two password not equal")
        if t == 0:
            raise("password error")
    def input_smtpserver(self):
        t = 3
        while t:
            t -= 1
            self.smtpserver = self.r_input('please input the smtp server:')
            self.port = self.r_input('please input the smtp server port:')
            try:
                self.smtp.connect(self.smtpserver, self.port)
            except Exception as e:
                print e
            else:
                break
        if t == 0:
            raise("smtp error")
class sendMail(MailConf):
    def __init__(self,receive_mail,subject,text = None,annexs = None):
        super(sendMail,self).__init__()
        # self.mail = MailConf()
        self.receive_email = receive_mail
        self.message = MIMEMultipart()
        self.message['From'] = Header(self.email,'utf-8')
        self.message['To'] = Header(receive_mail,'utf-8')
        self.message['Subject'] = Header(subject,'utf-8')
        self.message['text'] = Header(text,'utf-8')
        self._add_text(text)
        self._add_annex(annexs)

        self._send()
    def _add_text(self,text):
        self.message.attach(MIMEText(text, 'plain', 'utf-8'))
    def _add_annex(self,annexs):
        if annexs == None:
            return
        for annex in annexs:
            filename = annex
            print(filename)
            data = open(filename,'rb')
            ctype,encoding = mimetypes.guess_type(filename)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-steam'
            maintype,subtype = ctype.split('/',1)
            file_msg = MIMEBase(maintype,subtype)
            file_msg.set_payload(data.read())
            data.close()
            file_msg.add_header('Content-disposition','attachment',filename=os.path.basename(filename))
            self.message.attach(file_msg)
            print 'message add annex{}'.format(filename)
    def _send(self):
        # self.smtp.connect(self.mail.smtpserver,self.mail.port)
        # self.smtp.login(self.mail.mail,self.password)
        self.smtp.sendmail(self.email,self.receive_email,self.message.as_string())
        self.smtp.quit()

if __name__ == "__main__":
    receive_email = sys.argv[1] if len(sys.argv)>1 else None
    subject = sys.argv[2] if len(sys.argv)>2 else None
    text = sys.argv[3] if len(sys.argv)>3 else None
    annexs_str = sys.argv[4] if len(sys.argv)>4 else None
    annexs_list = annexs_str.split(";") if annexs_str else None
    sendMail(receive_email,subject,text,annexs_list)
