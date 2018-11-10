#coding:utf-8
import requests
import json
import os
import re
from bs4 import BeautifulSoup as bf
def listdir(path):  #传入存储的list
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if not os.path.isdir(file_path):
            list_name.append(file_path)
    return list_name

def get_all_page_soups(f_path):
    with open(f_path,'r') as f:
        js = json.load(f)
    urls = js['urls']
    atlas_url = []
    soups = []
    for url in urls:
        print url
        req = requests.get(url)
        soup = bf(req.text,'html.parser')
        soups.append(soup)
    return soups
def get_atlas_info(soups):
    # print soup
    atlas_info_list = []
    for soup in soups:
        atlas_info_list.extend(soup.select('ul > li > .bus_vtem'))
    print len(atlas_info_list)
    return atlas_info_list
def check_dir(dir):

    dir =  dir
    if not os.path.exists(dir):
    #     print dir
    #     os.mkdir(unicode(dir,"utf8"))
        os.mkdir(dir)
def parse_atlas_info_bus(atlas_info_list):
    atlas_info_dict_list = []
    print 1
    for atlas_info in atlas_info_list:
        atlas_info_dict = {}
        a_url = atlas_info.find('a').get('href')
        # print a_url
        a_title = atlas_info.find('a').get('title')
        a_preview_url = atlas_info.find('img').get('src')
        # print a_title
        # print a_preview_url
        atlas_info_dict['url'] = a_url
        atlas_info_dict['title'] = a_title
        atlas_info_dict['preview'] = a_preview_url
        atlas_info_dict_list.append(atlas_info_dict)
    return atlas_info_dict_list
theme_all_url_info_dir = 'theme_all_url_info'
list_name = listdir(theme_all_url_info_dir)
for theme_name in list_name:
    soups = get_all_page_soups(theme_name)
    atlas_info_list = get_atlas_info(soups)
    atlas_info_dict_list = parse_atlas_info_bus(atlas_info_list)
    for atlas_info_dict in atlas_info_dict_list:
        title = atlas_info_dict['title']
        title = ''.join(re.split('[ //\[\]]',title))
        print title
        path_list = os.path.split(theme_name)
        check_dir(path_list[1])
        atlas_info_dict_path =  os.path.join(path_list[1],title.encode("utf8"))
        print atlas_info_dict_path
        with open(atlas_info_dict_path,'w') as f:
            json.dump(atlas_info_dict,f)
