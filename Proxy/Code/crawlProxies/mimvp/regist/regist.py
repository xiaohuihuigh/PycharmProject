
from Code.session import Session
import json
import platform
if platform.python_version()[0] == '3':
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser
from Code import etc
import time
import random
loginfo = etc.loginfo
logerr = etc.logerr
class Regist(object):
    def __init__(self):
        cf = ConfigParser()
        cf.read('regist.conf')
        proxies = {
            'http': 'http://' + '27.24.197.129' + ':' + '9000'
        }
        self.sess =Session(has_proxy=True,proxies=proxies)
        self.regist_url = cf.get('regist','regist_url')
        self.vc_url = cf.get('regist','vc_url')
        self.regist_check_url = cf.get('regist','regist_check_url')
        self.run()
        print(self.sess.proxies)
        print(self.sess.cookies)
    def GetVc(self):
        res = self.sess.get(self.vc_url)
        with open('validatecode.png','wb') as f:
            f.write(res.content)
        return str(input('input the validatecode:'))
    @staticmethod
    def create_random_str(num1=3,num2=5):
        choice_str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        a = "".join([random.choice(choice_str1) for i in range(random.randint(num1,num2))])
        return a
    @staticmethod
    def create_random_telphone_num():
        choice_str1 = ['139', '138', '187']
        a = random.choice(choice_str1)
        choice_str1 = '1234567890'
        a = a + "".join([random.choice(choice_str1) for i in range(8)])
        return a
    @staticmethod
    def create_random_password(num1=3,num2=4,num3=4):
        str1 = 'abcdefghijklmnopqrstuvwxyz'
        str2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        str3 = '1234567890'
        b = "".join([random.choice(str1) for i in range(num1)])
        b = b+ "".join([random.choice(str2) for i in range(num2)])
        b = b+ "".join([random.choice(str3) for i in range(num3)])
        return b
    def create_user(self):
        a = self.create_random_str(5,10)
        b = self.create_random_str()
        c = self.create_random_str()
        email = '{}@{}.{}'.format(a,b,c)
        password = self.create_random_password()
        telphone = self.create_random_telphone_num()
        return email,password,telphone
    def run(self):
        self.sess.get(self.regist_url)
        time.sleep(3)
        email,password,telphone = self.create_user()
        vccode = self.GetVc()
        data = {
            'user_email': email,
            'user_pwd': password,
            'user_mobile': telphone,
            'user_rcode': vccode,
            'forurl': 'login.php'
        }
        rsp = self.sess.post(self.regist_check_url,data)
        rsp_j = json.loads(rsp.text)
        if rsp_j['Code'] != 0:
            logerr.error(rsp.text)

if __name__ == "__main__":
    Regist()
    #http://www.xdaili.cn/monitor