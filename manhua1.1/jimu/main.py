#coding:utf8
from bs4 import BeautifulSoup as bf
import json
import requests
from get_page_url_info import *
import etc
data_path = etc.data_path
manhua_url = etc.manhua_url
manhua_json_path = etc.manhua_json_path
def get_zhang_url_info():
    ans = requests.get(manhua_url)
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
    with open(os.path.join(data_path,manhua_json_path),'w')as f:
        json.dump(zhang_url_dict,f)

def get_page_url_info():
    with open(os.path.join(data_path,manhua_json_path),'r')as f:
        zhang_url_dict = json.load(f)
    main_url = etc.main_url
    for zhang_url in zhang_url_dict:
        print zhang_url
        url =main_url+zhang_url_dict[zhang_url]
        get_zhang_info(url)
def check_file(f_path):
    if not os.path.exists(f_path):
        dict = {'-1':1}
        with open(f_path,'w')as f:
            json.dump(dict,f)
def check_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
def down_the_manhua():
    check_dir(data_path)
    if not os.path.exists(manhua_json_path):
        get_zhang_url_info()
    get_page_url_info()
# def download_img():
down_the_manhua()