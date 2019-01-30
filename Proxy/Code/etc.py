#coding:utf-8
import os.path as op
import logging.config
pwd = op.abspath(op.dirname(__file__))
parent = op.abspath(op.dirname(pwd))

code_path = pwd
config_path = op.join(parent,'config')
log_path = op.join(config_path,'log')
doc_path = op.join(config_path,'doc')
conf_path = op.join(config_path,'conf')

redis_host = '127.0.0.1'
redis_db = 0
redis_psw = 'zyh'
redis_port = 6379
s_89ip_url = 'http://www.n89ip.cn/index_{}.html'
s_kuaidaili_inha_url = 'http://www.kuaidaili.com/free/inha/{}/'
s_kuaidaili_intr_url = 'http://www.kuaidaili.com/free/intr/{}/'
proxy_path = 'os.path.'

goubanjia_url = 'http://www.goubanjia.com/'
seofangfa_url = 'http://ip.seofangfa.com/'

mimvp_api_url = 'https://proxyapi.mimvp.com/api/fetchopen.php?orderid=866134503914150100&num=185&http_type=1&anonymous=5&result_fields=1,2,3,4,5,7&result_format=json'
# verified_url = "http://www.baidu.com"
verified_url = "http://www.baidu.com"
test_url = 'http://ip.seofangfa.com/checkproxy/'
# 数据库中代理的有效时间
alternate_effective_time = 60*60*24
immediate_effective_time = 300
to_use_effective_time = 120
crawl_effective_time = 600
#alternate queue中的最少数据和每次更新的个数
alternate_mlen = 600
alternate_llen = 2000
#immediate queue中的最少的数据和每次更新的个数
immediate_mlen = 100
immediate_llen = 200

crawl_mlen = 5000
crawl_llen = 10000
alternate_sleep_time = 10
immediate_sleep_time = 10
crawl_sleep_time=60
immediate_db = 0
alternate_db = 1
crawl_db = 2

info_list = ['IP','port','anonymity','ptype','locate','resspeed']
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
has_proxy = True
logfile=op.join(log_path,'logging.conf')
logging.config.fileConfig(logfile)
loginfo = logging.getLogger('info')
logerr = logging.getLogger('error')
logipinfo = logging.getLogger('ip')

# asdfasdg34234ASD 14/356
