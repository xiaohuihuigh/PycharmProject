#coding:utf-8
import requests
import chardet
import os
import re
from bs4 import BeautifulSoup as bf
# print requests.get('https://www.aisinei.org/thread-3848-1-1.html').text
def get_html_source_text(url):
    source = requests.get(url)
    return source
def get_mig_dir(soup):
    title = soup.select_one('head > title')
    title_name= title.get_text()
    print re.split('[ //\[\]]',title_name)
    title = ''.join(re.split('[ //\[\]]',title_name))
    print title
    return title
def get_img_info(soup):
    list_xw1 = soup.select('.mbn > .xw1')
    l = []
    for i in list_xw1:
        url = i.get('href')
        name = i.get_text()
        l.append({'url':url,'name':name})
    return l
def check_dir(dir):

    dir =  dir.encode("utf8")
    if not os.path.exists(dir):
    #     print dir
    #     os.mkdir(unicode(dir,"utf8"))
        os.mkdir(dir)


def save_img(dir,name,url):
    path = os.path.join(dir,name)
    print path
    text = requests.get(url).content
    with open(unicode(path.encode("utf8"), "utf8"), 'wb') as f:
        f.write(text)

def download_img(url):
    source = get_html_source_text(url)
    # print source.text
    soup = bf(source.text,'html.parser')
    # bf(res.text, 'html.parser')
    dir_name = get_mig_dir(soup)
    img_info_list = get_img_info(soup)
    for img_info in img_info_list:
        img_url = img_info['url']
        name = img_info['name']
        check_dir(dir_name)
        save_img(dir_name,name,img_url)
if __name__ == '__main__':
    download_img("https://www.aisinei.org/thread-6944-1-1.html")