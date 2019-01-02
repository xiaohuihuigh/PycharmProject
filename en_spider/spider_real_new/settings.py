# -*- coding: utf-8 -*-

import os
import sys
import MySQLdb
import logging
from logging import config
from warnings import filterwarnings

PATH = os.path.dirname(os.path.abspath(__file__))
print PATH
sys.path.append(PATH)
print(PATH)
#logging.config.fileConfig(PATH + "/log/logging.conf")
logger = logging.getLogger("spider")


# mysql设置
MASTER_MYSQL_ARGS = {
    'host': 'localhost',
    'user': 'develop',
    'passwd': 'sd61131707',
    'db': 'spider_data',
    'charset': 'utf8'
}

NEWS_MYSQL_ARGS = MASTER_MYSQL_ARGS

con = MySQLdb.connect(**NEWS_MYSQL_ARGS)    # NEWS_MYSQL_ARGS is the keyword para so that we use the **kw

CON = con

TBB = "spider_news"

PAGE_TABLE = "news_url_content"

PAGE_TABLE_NEW = "url"

# 忽略mysql警告
filterwarnings('ignore', category=MySQLdb.Warning)

logger.info("setting initialize")

SLOW_TIME = 10
CONCURRENT_REQUESTS = 64
CONCURRENT_PER_REQUESTS = 8
CONCURRENT_ITEMS = 128

# html保存
HTML_DIR = "/root/spider_source/spider_real_new/htmls"


# redis缓存设置
RS_DB = {
    "host": "localhost",
    "port": 6379,
    "db": 2
}

