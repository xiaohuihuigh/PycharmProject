#https://proxy.mimvp.com/usercenter/regist.php
import session
import requests
from requests.cookies import RequestsCookieJar
import json
regist_url = 'https://proxy.mimvp.com/usercenter/regist.php'
vc_url = 'https://proxy.mimvp.com/common/ygrcode.php'
regist_check_url = 'https://proxy.mimvp.com/lib/user_regist_check.php'
login_check_url = 'https://proxy.mimvp.com/lib/user_login_check.php'
user_info_url = 'https://proxy.mimvp.com/usercenter/userinfo.php'
def ReadCookies():
    jar = RequestsCookieJar()
    try:
        with open('cookies.txt','r')as f:
            cookies = json.load(f)
            for cookie in cookies:
                jar.set(cookie,cookies[cookie])
    except:
        print "None"
        return None
    return jar
def CheckCookies(session):
    return True
def SaveCookies(cookies):
    print 'save cookies', cookies
    cookies = requests.utils.dict_from_cookiejar(cookies)
    # print cookies
    try:
        with open('cookies.txt', 'w') as f:
            json.dump(cookies, f)
    except:
        # print 'save cookie error'
        return False
    return True
def RenewCookies(sess):
    SaveCookies(sess.get(regist_url).cookies)
def GetCookies():
    sess = session.Session(has_proxy=True)
    cookie = ReadCookies()
    if cookie != None:
        sess.cookies = cookie
        # if (CheckCookies(session)):
        #     return session
    else:
        RenewCookies(sess)
        cookie = ReadCookies()
        sess.cookies = cookie
    return sess
def GetVc(session):
    print 'getvccookies',session.cookies
    res = session.get(vc_url)
    with open('validatecode.png','wb') as f:
        f.write(res.content)
    return str(raw_input('input the validatecode:'))



sess = GetCookies()
# vccode = GetVc(sess)
# data = {
# 'user_email': 'asedf@asd.asd',
# 'user_pwd': '2r7SaDT4R6fwT9J',
# 'user_mobile': '17818711568',
# 'user_rcode': vccode,
# 'forurl': 'login.php'
#
# }
# rep = sess.post(regist_check_url,data=data)
# print rep.text
# print sess.cookies
data = {
'user_email': 'asedf@asd.asd',
'user_pwd': '2r7SaDT4R6fwT9J',

}
# sess.post(login_check_url,data=data)
rep = sess.get('https://proxyapi.mimvp.com/api/fetchopen.php?orderid=868050401999005103&num=20&http_type=1&ping_time=0.3&result_fields=1,2')
print rep.text
print sess.cookies
'''
https://proxyapi.mimvp.com/api/fetchall.php?orderid=866020440901107493&num=2&filter_hour=12&result_fields=1,2,3
https://proxyapi.mimvp.com/api/fetchsole.php?orderid=866020440901107493&num=2&result_fields=1,8,2,3
https://proxyapi.mimvp.com/api/fetchsecret.php?orderid=866020440901107493&num=5&result_fields=1,2,3
https://proxyapi.mimvp.com/api/fetchopen.php?orderid={}&num={}&result_fields={}
{"code":0,"code_msg":"\u63d0\u53d6\u6210\u529f","expire_dtime":"2019-01-04 14:47:14","today_fetch_num":94,"today_total_num":5000,"dtime":"2019-01-04 10:47:14","url":"https:\/\/proxy.mimvp.com","
request":{"orderid":"866020440901107493","user_email":"asdf@asd.asd","user_type":"free","num":"20","port":"","country":"","country_group":"0","http_type":"1","anonymous":"0","isp":"0","ping_time":"0","transfer_time":"0","request_method":"0","check_success_count":"0","result_fields":"1,2,3,4,5,6,7,8,9","result_sort_field":"1","result_format":"json","result_format_need_request":"1","filter_hour":"1"},"cost_time":"2.206783","result":[{"check_total_count":1,"check_success_ratio":1,"transfer_time":9.968631,"ping_time":999999,"check_success_count":1,"check_dtime":20181229003503,"ip:port":"106.12.97.93:8888","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u767e\u5ea6\u4e91","country":"\u4e2d\u56fd:\u5e7f\u4e1c"},{"check_total_count":5,"check_success_ratio":1,"transfer_time":13.714866,"ping_time":0.139875,"check_success_count":5,"check_dtime":20181229002143,"ip:port":"110.52.234.132:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":1,"check_success_ratio":1,"transfer_time":0.336881,"ping_time":999999,"check_success_count":1,"check_dtime":20181228235326,"ip:port":"111.177.182.76:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u7535\u4fe1","country":"\u4e2d\u56fd:\u6e56\u5317"},{"check_total_count":1,"check_success_ratio":1,"transfer_time":0.65206,"ping_time":999999,"check_success_count":1,"check_dtime":20181228232356,"ip:port":"140.143.96.108:1080","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u817e\u8baf\u4e91","country":"\u4e2d\u56fd:\u56db\u5ddd"},{"check_total_count":1,"check_success_ratio":1,"transfer_time":1.021287,"ping_time":999999,"check_success_count":1,"check_dtime":20181228230033,"ip:port":"119.27.174.56:1080","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u817e\u8baf\u4e91","country":"\u4e2d\u56fd:\u56db\u5ddd"},{"check_total_count":47,"check_success_ratio":0.851063829787234,"transfer_time":7.742656,"ping_time":0.027949,"check_success_count":40,"check_dtime":20181228215015,"ip:port":"60.173.244.133:35634","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u7535\u4fe1","country":"\u4e2d\u56fd:\u5b89\u5fbd"},{"check_total_count":34,"check_success_ratio":0.47058823529411764,"transfer_time":0.306862,"ping_time":0.043983,"check_success_count":16,"check_dtime":20181228214734,"ip:port":"47.95.157.182:3200","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u963f\u91cc\u4e91","country":"\u4e2d\u56fd:\u5317\u4eac"},{"check_total_count":1,"check_success_ratio":1,"transfer_time":13.830946,"ping_time":999999,"check_success_count":1,"check_dtime":20181228201148,"ip:port":"39.108.221.96:8088","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u963f\u91cc\u4e91","country":"\u4e2d\u56fd:\u5e7f\u4e1c"},{"check_total_count":3,"check_success_ratio":1,"transfer_time":12.271086,"ping_time":0.049222,"check_success_count":3,"check_dtime":20181228182246,"ip:port":"119.39.238.5:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":4,"check_success_ratio":1,"transfer_time":5.321748,"ping_time":999999,"check_success_count":4,"check_dtime":20181228171448,"ip:port":"110.52.234.209:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":8,"check_success_ratio":1,"transfer_time":5.574626,"ping_time":0.03864,"check_success_count":8,"check_dtime":20181228155413,"ip:port":"110.52.234.195:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":6,"check_success_ratio":1,"transfer_time":13.670319,"ping_time":0.032994,"check_success_count":6,"check_dtime":20181228145054,"ip:port":"110.52.234.129:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":1,"check_success_ratio":1,"transfer_time":0.36711,"ping_time":999999,"check_success_count":1,"check_dtime":20181228143211,"ip:port":"111.177.174.172:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u7535\u4fe1","country":"\u4e2d\u56fd:\u6e56\u5317"},{"check_total_count":1,"check_success_ratio":1,"transfer_time":8.067318,"ping_time":999999,"check_success_count":1,"check_dtime":20181228142540,"ip:port":"111.177.171.35:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u7535\u4fe1","country":"\u4e2d\u56fd:\u6e56\u5317"},{"check_total_count":15,"check_success_ratio":0.6,"transfer_time":10.133984,"ping_time":0.033977,"check_success_count":9,"check_dtime":20181228125307,"ip:port":"119.122.213.38:9000","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u7535\u4fe1","country":"\u4e2d\u56fd:\u5e7f\u4e1c"},{"check_total_count":9,"check_success_ratio":0.8888888888888888,"transfer_time":0.836555,"ping_time":999999,"check_success_count":8,"check_dtime":20181228121906,"ip:port":"110.52.234.55:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":6,"check_success_ratio":0.8333333333333334,"transfer_time":0.467846,"ping_time":999999,"check_success_count":5,"check_dtime":20181228073811,"ip:port":"110.52.234.79:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":4,"check_success_ratio":1,"transfer_time":3.338184,"ping_time":999999,"check_success_count":4,"check_dtime":20181228040312,"ip:port":"110.52.234.140:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"},{"check_total_count":1,"check_success_ratio":1,"transfer_time":6.779632,"ping_time":999999,"check_success_count":1,"check_dtime":20181228010534,"ip:port":"111.198.77.169:50326","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u5317\u4eac"},{"check_total_count":4,"check_success_ratio":1,"transfer_time":4.668444,"ping_time":0.015802,"check_success_count":4,"check_dtime":20181228002919,"ip:port":"110.52.234.32:9999","http_type":"HTTPS","anonymous":"\u9ad8\u533f","isp":"\u8054\u901a","country":"\u4e2d\u56fd:\u6e56\u5357"}],
"result_count":20}
'''