#coding:utf-8
import json
from download_atlas import *
import os


def listdir(path):  #传入存储的list
    list_name = []
    if os.path.exists(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if not os.path.isdir(file_path):
                list_name.append(os.path.split(file_path)[1])
    return list_name
def check_file(file_path):
    if os.path.exists(file_path):
        return
    sample = os.path.join(check_main,'check')
    open(file_path, "wb").write(open(sample, "rb").read())
def check_down(check_path,fod):
    check_file(check_path)
    with open(check_path,'r') as f:
        t = json.load(f)
        if unicode(fod,"utf8") in t and t[unicode(fod,"utf8")] == '1':
            return True
    return False


def had_down(check_path,fod):
    check_file(check_path)
    with open(check_path,'r') as f:
        t = json.load(f)
    with open(check_path,'w') as f:
        t[fod] = '1'
        print t
        json.dump(t,f)
def get_atlas_url(atlas_url_path):
    with open(atlas_url_path,'r')as f:
        js = json.load(f)
        return js['url']
main_path = 'theme_all_url_info'
theme_list = listdir(main_path)
check_main = 'check_download'

for theme in theme_list:
    if check_down(os.path.join(check_main,'theme'),theme):
        print "check had down the theme",theme
        continue
    print "check not down the theme",theme
    atlas_list = listdir(theme)
    # print atlas_list
    for atlas in atlas_list:
        # print atlas
        if check_down(os.path.join(check_main, theme), atlas):
            print "check_had_down the atlas",atlas
            continue
        print "check not down",atlas
        atlas_url_path = os.path.join(theme,atlas)
        print atlas_url_path
        url = get_atlas_url(atlas_url_path)
        print url
        download_img(url)
        print 'down load the atlas'+atlas
        had_down(os.path.join(check_main,theme),atlas)
    had_down(os.path.join(check_main,'theme'),theme)
