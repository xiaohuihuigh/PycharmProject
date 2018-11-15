#coding:utf8
import os
#
manhua_name = 'momv'

data_path = os.path.join("/home/zyh/Data/manhua/momv/")             #漫画存入的目录

manhua_url = "http://m.930mh.com/manhua/16465/" #漫画的主链接

main_url = 'http://m.930mh.com'                 #网站链接

#在序章中间加0
manhua_json_path="monv.json"                    #漫画每一个章节的章节名字和链接组成的json文件

phantomjs_path="/opt/phantomjs/bin/phantomjs"

zhang_check_path = "zhang_check"                #每一章的具体信息是否爬取的检查json

img_check_name = "img_check"



# data_path = "/home/zyh/Data/manhua/BAKHyeongJun/"             #漫画存入的目录
#
# manhua_url = "http://m.930mh.com/manhua/3857/" #漫画的主链接
#
# main_url = 'http://m.930mh.com'                 #网站链接
#
# #在序章中间加0
# manhua_json_path="BAKHyeongJun.json"                    #漫画每一个章节的章节名字和链接组成的json文件
#
# phantomjs_path="/opt/phantomjs/bin/phantomjs"
#
# zhang_check_path = "zhang_check"                #每一章的具体信息是否爬取的检查json
#
# img_check_name = "img_check"