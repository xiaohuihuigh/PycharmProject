# from Requests import Requests
import requests
import etc
from bs4 import BeautifulSoup as bf
import json
import os
import io
import time

def download_one_page(name,url):
    url = etc.website_url+url
    rsp = requests.get(url,timeout=10)
    html = rsp.text.encode('ISO-8859-1').decode('gbk').encode('utf-8').decode('utf-8')
    soup = bf(html,'html.parser')
    rsp = soup.select_one('.box_con > #content')
    rsp = rsp.text
    print(rsp)
    with io.open(name+'.txt','w',encoding='utf-8')as f:
        f.write(rsp)


def check_file(file_path):
    if os.path.exists(file_path):
        return
    sample = 'check.json'
    open(file_path, "wb").write(open(sample, "rb").read())

def check_down(check_path,fod):
    check_file(check_path)
    with open(check_path,'r') as f:
        t = json.load(f)
        if fod in t and t[fod] == '1':
            return True
    return False


def had_down(check_path,fod):
    check_file(check_path)
    with open(check_path,'r') as f:
        t = json.load(f)
    with open(check_path,'w') as f:
        t[fod] = '1'
        json.dump(t,f)


with open('url.json','r')as f:
    url_dict_list = json.load(f)
    check_file('check_down.json')
print('get the url.json')
for i, url_dict in enumerate(url_dict_list):
    #
    for url_info in url_dict.keys():
        if check_down('check_down.json',url_dict[url_info]):
            continue
        time.sleep(3)
        print(str(i)+'**'+url_info)
        download_one_page(str(i)+'**'+url_info,url_dict[url_info])
        had_down('check_down.json',url_dict[url_info])


