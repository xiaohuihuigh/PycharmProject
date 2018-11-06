#coding:utf8
import os
import requests
import re
from  selenium import webdriver
from bs4 import BeautifulSoup as bf
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
data_path = "/home/zyh/Data/manhua"
phantomjs_path = "/opt/phantomjs/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=phantomjs_path,desired_capabilities=dcap)

def get_page_source(driver,url):
    driver.get(url)
    pagesource = driver.page_source
    soup = bf(pagesource,'html.parser')
    return soup

def get_zhangjie(soup):
    text = soup.select_one('.BarTit').text
    pat = re.compile(r'\d+')
    findlist = re.findall(pat, text)
    return findlist[0]
def get_totle_page(soup):
    return soup.select_one('div > any').text
def get_img_url(soup):
    return soup.select_one('div > img').get('src')
def check_down(t):
    with open(os.path.join(data_path,'zhang_check'),'r')as f:
        dict = json.load(f)
    if t in dict:
        return True
    return False
def get_down(t):
    with open(os.path.join(data_path,'zhang_check'),'r')as f:
        dict = json.load(f)
    dict[t] = 1
    with open(os.path.join(data_path,'zhang_check'),'w') as f:
        json.dump(dict,f)
def get_zhang_info(url):
    soup = get_page_source(driver,url)
    # print soup
    zhang = get_zhangjie(soup)
    totle_page = get_totle_page(soup)
    img_dict = {}
    img_path = os.path.join(data_path,zhang)
    if check_down(zhang):
        print "had down this ",zhang,"zhang page url info"
        return
    for i in range(1,int(totle_page)+1):
        print i
        page_url = url+'?p='+str(i)
        print page_url
        img_url = get_img_url(get_page_source(driver,page_url))
        print img_url
        img_dict[i] = img_url
    with open(img_path+'_img_url_json','w')as f:
        json.dump(img_dict,f)
    get_down(zhang)
