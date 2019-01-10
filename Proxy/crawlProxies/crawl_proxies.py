#coding:utf-8
# from mimvp import mimvp
from crawlProxies.mimvp import mimvp
from crawlProxies.n89ip import n89ip
from crawlProxies.kuaidaili import crawl_kuaidaili_proxies,crawl_kuaidaili_proxies1
from crawlProxies import goubanjia
from crawlProxies import seofangfa
from multiprocessing import Process
from configparser import ConfigParser
from crawlProxies import crawl_proxies_conf
import time
import os
fp = 'crawlProxies/crawlProxies.conf'
conf = ConfigParser()
conf.read(os.path.join(os.getcwd(),fp))
ilist = dir()
[ilist.remove(i) for i in ['os','crawl_proxies_conf','conf','ConfigParser', 'Process', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'fp', 'time']]
conf.set('all','name',str(ilist))
with open(fp,'w')as f:
    conf.write(f)
crawl_proxies_conf.set_config()
def crawlProxies():
    ps = []
    global fp,conf
    conf.read(fp)
    iliststr = conf.get('all','name')
    iliststr = iliststr.strip('[]').split(', ')
    ilist = [i.strip("'") for i in iliststr]
    for i in ilist:
        yn = conf.get(i,'yn')
        if yn == 'True':
            last_time = conf.getint(i,'last_time')
            interval_time = conf.getint(i,'interval_time')
            now_time = int(time.time())
            if now_time - last_time > interval_time:
                ps.append(Process(target=globals()[i].crawl_proxies))
                conf.set(i,'last_time',str(now_time))
                with open(fp,'w')as f:
                    conf.write(f)
    # print(len(ps))
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    return len(ps)
if __name__ == '__main__':
    crawlProxies()