#coding:utf-8
website_url = 'http://www.biquge.com.tw'
main_url = 'http://www.biquge.com.tw/16_16876/'

import requests
import json
import re
from bs4 import BeautifulSoup as bf
def get_all_url():
    rsp = requests.get(main_url,timeout=10)
    rsp_html = rsp.text.encode('ISO-8859-1').decode('gbk').encode('utf-8').decode('utf-8')
    # print(rsp_html)
    soup = bf(rsp_html,'html.parser')
    # print(soup)
    # lists = soup.select_one('#list')
    # print(lists)
    lists = soup.select('div > dl > dd > a')



    print(lists)# pat = re.compile(r'第二章：千梅（1')
    # print(pat.findall(rsp_html))
    print(len(lists))
    url_dict_list = []
    for url in lists:
        url_dict = {}
        url_dict[url.text] = url.get('href')
        url_dict_list.append(url_dict)
    with open('url.json','w') as f:
        json.dump(url_dict_list,f)
    print(url_dict_list)
# get_all_url()