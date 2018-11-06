#coding:utf8
from bs4 import BeautifulSoup as bf
import json
import requests
from get_page_url_info import *
data_path = '/home/zyh/Data/manhua'
def get_zhang_url_info():
    ans = requests.get("http://m.930mh.com/manhua/14396/")
    soup = bf(ans.text,'html.parser')
    print ans.text
    soup = soup.select('div > ul')
    print soup
    url_list = soup[0].find_all('a')
    zhang_url_dict = {}
    for it in url_list:
        print it.text.strip()
        print it.get('href')
        zhang_url_dict[it.text.strip()] = it.get('href')
    with open('/home/zyh/Data/manhua/jimu.json','w')as f:
        json.dump(zhang_url_dict,f)

def get_page_url_info():
    with open('/home/zyh/Data/manhua/jimu.json','r')as f:
        zhang_url_dict = json.load(f)
    main_url = 'http://m.930mh.com'
    for zhang_url in zhang_url_dict:
        print zhang_url
        url =main_url+zhang_url_dict[zhang_url]
        get_zhang_info(url)
get_page_url_info()
# def download_img():
