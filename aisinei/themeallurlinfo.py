# -*- coding: utf-8 -*-
import requests
import json

import os
import os
def listdir(path):  #传入存储的list
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if not os.path.isdir(file_path):
            list_name.append(file_path)
    return list_name
list = listdir('theme_info')
print len(list)
theme_all_url_dir = 'theme_all_url_info'
for theme_info in list:
    with open(theme_info,'r') as f:
        t = json.load(f)
    print t
    urls = []
    num_url = (int(t[u"帖数:"])-1)/20+2
    for i in range(1,num_url):
        url = t[u"url"].replace('1',str(i))
        urls.append(url)
    t['urls'] = urls
    with open(os.path.join(theme_all_url_dir,t[u'name']),'w') as f:
        json.dump(t,f)