#coding:utf-8
#通过分类找到主题的基本信息以及有几个页面
import requests
import json
import os
from bs4 import BeautifulSoup as bf
url = 'https://www.aisinei.org/'

url_rm = 'https://www.aisinei.org/forum.php?gid=1'
url_xr = 'https://www.aisinei.org/forum.php?gid=56'
source = requests.get(url_xr)
soup = bf(source.text,'html.parser')
# print soup.text
theme_list = soup.select('tr > .fl_g > dl')
theme_info = []
for i in theme_list:
    theme_dic = {}
    a = i.select_one('dt > a')
    theme_url = a.get('href')
    theme_name = a.text
    ems = i.select('em')
    print theme_name
    print theme_url
    theme_dic['name']= theme_name
    theme_dic['url'] = theme_url
    for j in ems:
        text = j.text
        import re
        text =text.strip('')
        lt = re.split('[ ""\r\n/]',text)
        dl = [i for i in lt if i != '']
        print dl
        theme_dic[dl[0]] = dl[1]
    theme_info.append(theme_dic)
print theme_info

theme_info_dir = 'theme_info'

for i in theme_info:
        theme_name = i['name']
        # print theme_name
        theme_path = os.path.join(theme_info_dir,theme_name)
        with open(theme_path,'w') as f:
            json.dump(i, f)