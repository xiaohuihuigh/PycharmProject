#coding:utf-8
import os.path as op
import logging.config
import platform
if platform.python_version()[0] == '3':
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser


pwd = op.abspath(op.dirname(__file__))
parent = op.abspath(op.dirname(pwd))
grandparent = op.abspath(op.dirname(parent))
code_path = pwd
config_path = op.join(parent,'config')
log_path = op.join(config_path,'log')
doc_path = op.join(config_path,'doc')
conf_path = op.join(config_path,'conf')

conf = ConfigParser()
conf.read(op.join(conf_path,'proxies.conf'))
redis_db = conf.getint('redis','crawl_db')
redis_host = conf.get('redis','redis_host')
redis_psw = conf.get('redis','redis_psw')
redis_port = conf.getint('redis','redis_port')

s_89ip_url = conf.get('crawl_url','s_89ip_url')
s_kuaidaili_inha_url =  conf.get('crawl_url','s_kuaidaili_inha_url')
s_kuaidaili_intr_url = conf.get('crawl_url','s_kuaidaili_intr_url')

goubanjia_url = conf.get('crawl_url','goubanjia_url')
seofangfa_url = conf.get('crawl_url','seofangfa_url')

mimvp_api_url = conf.get('crawl_url','mimvp_api_url')
# verified_url = "http://www.baidu.com"
verified_url = conf.get('crawl_url','verified_url')
test_url = conf.get('crawl_url','test_url')
# 数据库中代理的有效时间
alternate_effective_time = conf.getint('alternate_process','alternate_effective_time')
immediate_effective_time = conf.getint('immediate_process','immediate_effective_time')
to_use_effective_time = conf.getint('to_use_process','to_use_effective_time')
crawl_effective_time = conf.getint('crawl_process','crawl_effective_time')
#alternate queue中的最少数据和每次更新的个数
alternate_mlen = conf.getint('alternate_process','alternate_mlen')
alternate_llen = conf.getint('alternate_process','alternate_llen')
#immediate queue中的最少的数据和每次更新的个数
immediate_mlen = conf.getint('immediate_process','immediate_mlen')
immediate_llen = conf.getint('immediate_process','immediate_llen')

crawl_mlen = conf.getint('crawl_process','crawl_mlen')
crawl_llen = conf.getint('crawl_process','crawl_llen')
alternate_sleep_time = conf.getint('alternate_process','alternate_sleep_time')
immediate_sleep_time = conf.getint('immediate_process','immediate_sleep_time')
crawl_sleep_time= conf.getint('crawl_process','crawl_sleep_time')
immediate_db = conf.getint('redis','immediate_db')
alternate_db = conf.getint('redis','alternate_db')
crawl_db = conf.getint('redis','crawl_db')

# info_list = ['IP','port','anonymity','ptype','locate','resspeed']
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# has_proxy = True
logfile=op.join(log_path,conf.get('log_conf','log_conf_file'))
logging.config.fileConfig(logfile)
loginfo = logging.getLogger('info')
logerr = logging.getLogger('error')
logipinfo = logging.getLogger('ip')

# asdfasdg34234ASD 14/356
# redis_host = 127.0.0.1
# redis_psw = redisredis
# redis_port = 6379