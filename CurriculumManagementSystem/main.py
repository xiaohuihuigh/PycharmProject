#coding:utf-8
import BeautifulSoup
import requests
from requests.cookies import RequestsCookieJar
import time
import re
import os
import sys
import json
from generic_variables import *
'''
get a raw_inpupt

return the striped string from the raw_input
'''
def GetRawInput(str = ''):
    message = str(raw_input(str))
    return message.strip()
'''
Read the recorded Cookies values

if get the cookies then return it 
else return None
'''
def ReadCookies():
    jar = RequestsCookieJar()
    try:
        with open('cookies.txt','r') as f:
            cookies = json.load(f)
            # print type(cookies)

            for cookie in cookies:
                # print cookie
                # jar.set(cookie["name"],cookie["value"])
                jar.set(cookie,cookies[cookie])
                # print jar
    except :
        # print 'get cookie error'
        return None
    return jar
'''
Save the Cookies value 

get a cookies and save it to 'cookies.txt' file
if saved successfully return True
else return False
'''
def SaveCookies(cookies):
    print 'save cookies',cookies
    cookies = requests.utils.dict_from_cookiejar(cookies)
    # print cookies
    try:
        with open('cookies.txt','w') as f:
            json.dump(cookies,f)
    except :
        # print 'save cookie error'
        return False
    return True

'''
Update the cookies value through access the LoginUrl and call SaveCookies
'''
def RenewCookies():
    # print 'renew the cookies'
    SaveCookies(requests.get(LoginUrl).cookies)
'''
check whether the cookies is valuable 

get the session(have the cookies)
if the session can get the home page return True
else return False
'''
def CheckCookies(session):
    print 'CheckCookies',session.cookies

    rsq  =session.get(LoginUrl+'/Home/StudentIndex')
    rr = re.compile(r'1\d{7}')
    # print rsq.content
    s = rr.findall(rsq.content)
    # print s
    if s != []:
        return True
    else :
        return False
'''
get the session that has the valuable cookies to login    
'''
def GetSession():
    session = requests.session()
    cookie = ReadCookies()
    if cookie != None :
        # print 'cookie is not none'
        session.cookies = cookie
        if (CheckCookies(session)):
            # print 'check login seccess'
            return session
        else:
            RenewCookies()
            cookie = ReadCookies()
            session.cookies = cookie
            LoginCMS(session)
            if (CheckCookies(session)):
                return session
    RenewCookies()
    GetSession()



'''
to get login the CurriculumManagementSystem

get a session that hasn't been logged in yet
get the Username and Password through input 
return a response from login
'''
def LoginCMS(session):
    UserName = GetRawInput('input the Username:')
    UserPassword = GetRawInput('input the Password:')
    ValidateCode = GetVc(session)
    print 'logincmscookie:',session.cookies
    parms = {'txtUserName':UserName,'txtPassword':UserPassword,'txtvaliCode':ValidateCode}
    return session.post(LoginUrl,parms)
'''
get the ValidateCode

get the validatecode through input and return it
'''
def GetVc(session):
    print 'getvccookie:',session.cookies
    res = session.get(LoginUrl+ValidateCodeUrl)
    with open('validatecode.png','wb') as f:
        f.write(res.content)
    return str(raw_input('input the validatecode:'))

'''
get the student course table message

get the logged session and access the trul url
save the response to a html file
'''
def GetCrouseTable(session):
    QueryCTUrl = LoginUrl+QueryCourseTableUrl
    # QueryCTUrl = 'http://xk.autoisp.shu.edu.cn:8080/StudentQuery/CtrlViewQueryCourseTable'
    rsp = session.get(QueryCTUrl)
    # print rsp.content
    with open('coursetable.html', 'wb')as f:
        f.write(rsp.content)
'''
get the student course rank table message

get the logged session and access the trul url
save the response to a html file
'''
def GetEnrollRankTable(session):
    QueryERUrl = LoginUrl+QueryEnrollRankUrl
    rsp = session.get(QueryERUrl)
    # print rsp.content
    with open('enrollranktable.html', 'wb')as f:
        f.write(rsp.content)
'''
get the student deleted course table message

get the logged session and access the trul url
save the response to a html file
'''
def GetDeleteCourseTable(session):
    QueryERUrl = LoginUrl+QueryDeleteCourseUrl
    rsp = session.get(QueryERUrl)
    # print rsp.content
    with open('deletecoursetable.html', 'wb')as f:
        f.write(rsp.content)
'''
get the student deleted course table message

get the logged session and access the trul url
save the response to a html file
'''

def GetQueryParmsData():
    ParmsName = ['CourseNo', 'CourseName', 'TeachNo', 'TeachName',
                 'CourseTime', 'NotFull', 'Credit', 'Campus', 'Enrolls',
                 'DataCount', 'MinCapacicy', 'MaxCapacity', 'PageIndex',
                 'PageSize', 'FunctionString']
    # ParmsValue = ['12', '', '', '',
    #               '', 'false', '', '0', '',
    #               '0', '', '', '1',
    #               '1000', 'InitPage']
    parms = {}
    for i in ParmsName:
        if i == 'NotFull':
            print i ,":0 is false and 1 is true,default false"
            print "input your choose [0/1]:"
            ForT = GetRawInput()
            parms[i] = 'false'
            if ForT == 1:
                parms[i] = 'true'
        elif i == 'Campus':
            print i,":get 7 choose"
            print "0：全部  1：本部  2：延长  3：嘉定  4：待用  5：徐经  6：宝山东校区"
            print "input you choose [0-6]:"
            ChooseCampus = GetRawInput()
            if ChooseCampus!='':
                parms[i] = ChooseCampus
            else:
                parms[i] = 0
        elif i == 'DataCount':
            print i,":0 is not limit and other num is the response data num"
            LimitDataCount = GetRawInput()
            if LimitDataCount != '':
                parms[i] = LimitDataCount
            else:
                parms[i] = 0
        elif i == 'PageSize':
            print i,"default 20:"
            PageSize = GetRawInput()
            if PageSize != '':
                parms[i] = PageSize
            else:
                parms[i] = 20
        elif i == 'FunctionString':
            parms[i] = 'InitPage'
        elif i == 'PageIndex':
            PageIndex = GetRawInput()
            if PageIndex != '':
                parms[i] = PageIndex
            else:
                parms[i] = 1
        else:
            print i,":"
            parms[i] = GetRawInput()
    return parms
'''

'''
def GetQueryCourseTable(session):
    QueryERUrl = LoginUrl+QueryCourseTUrl
    # QueryERUrl ='http://xk.autoisp.shu.edu.cn:8080/StudentQuery/CtrlViewQueryCourse'
    headers = {
        "Host": "xk.autoisp.shu.edu.cn:8080",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://xk.autoisp.shu.edu.cn:8080/StudentQuery/QueryCourse",
        "Content-Length": "181",
    }
    parms = GetQueryParmsData()
    rsp = session.post(QueryERUrl,parms,headers=headers)
    print rsp.content

    with open('querycoursetable.html', 'wb')as f:
        f.write(rsp.content)
'''

'''
def ValiWhereValue(session):
    QueryERUrl = 'http://xk.autoisp.shu.edu.cn:8080/Login/ValiWhereValue'
    headers = {
        "Host": "xk.autoisp.shu.edu.cn:8080",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://xk.autoisp.shu.edu.cn:8080/StudentQuery/QueryCourse",
        "Content-Length": "121",
    }
    ParmsName = ['CourseNo','CourseName','TeachNo','TeachName',
                 'CourseTime','NotFull','Credit','Campus','Enrolls',
                 'MinCapacicy','MaxCapacity']
    # ParmsValue = []
    ParmsValue = ['12', '', '', '',
                 '', 'false', '', '0', '','','',]
    parms = {}
    for i in range(len(ParmsName)):
        print "input the ",ParmsName[i],":"
        # parms[ParmsName[i]] = GetRawInput()
        print ParmsValue[i]
        parms[ParmsName[i]] = ParmsValue[i]
    print parms
    rsp = session.post(QueryERUrl,data=parms,headers = headers)
    print rsp.content

    with open('vali.html', 'wb')as f:
        f.write(rsp.content)
'''

'''
if __name__ == '__main__':
    session = GetSession()
    GetCrouseTable(session)
    GetEnrollRankTable(session)
    GetDeleteCourseTable(session)
    # ValiWhereValue(session)
    GetQueryCourseTable(session)