#coding:utf8
import os
import requests
import re
from  selenium import webdriver
from bs4 import BeautifulSoup as bf
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import etc
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
data_path = etc.data_path

# req = requests.get(pageImage)
# with open(os.path.join(data_path,'img.jpg'),'w') as f:
#     f.write(req.content)
phantomjs_path = etc.phantomjs_path
driver = webdriver.PhantomJS(executable_path=phantomjs_path,desired_capabilities=dcap)
zhang_check_path = os.path.join(data_path,etc.zhang_check_path)
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
def check_file(zhang_check_path):
    print "checkfile"
    print os.path.exists(zhang_check_path)
    if not os.path.exists(zhang_check_path):
        print "not existfile",zhang_check_path
        dict = {}
        dict['-1'] = 1
        with open(zhang_check_path,'w')as f:
            json.dump(dict,f)

def check_down(t):
    with open(zhang_check_path,'r')as f:
        dict = json.load(f)
    if t in dict:
        return True
    return False
def get_down(t):
    with open(zhang_check_path,'r')as f:
        dict = json.load(f)
    dict[t] = 1
    with open(zhang_check_path,'w') as f:
        json.dump(dict,f)
def get_zhang_info(url):
    print zhang_check_path
    print os.path.exists(zhang_check_path)
    soup = get_page_source(driver,url)
    # print soup
    zhang = get_zhangjie(soup)
    totle_page = get_totle_page(soup)
    img_dict = {}
    img_path = os.path.join(data_path,zhang)
    print totle_page
    print img_path
    check_file(zhang_check_path)
    get_down('-1')
    if check_down(zhang):
        print "had down this ",zhang,"zhang page url info"
        return

    for i in range(1,int(totle_page)+1):
        print i
        # check_down_img(str(i))
        page_url = url+'?p='+str(i)
        print page_url
        with open(img_path+'_img_url_json')as f:
            i_dict = json.load(f)
        if i in i_dict:
            print "had down the page ",i
            continue
        img_url = get_img_url(get_page_source(driver,page_url))
        print img_url
        img_dict[i] = img_url
        with open(img_path + '_img_url_json', 'w')as f:
            json.dump(img_dict, f)
        # had_down_img(str(i))

    get_down(zhang)
