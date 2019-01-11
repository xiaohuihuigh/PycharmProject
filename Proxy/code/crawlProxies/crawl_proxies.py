#coding:utf-8
# from mimvp import mimvp

from code.crawlProxies.mimvp import mimvp
from code.crawlProxies.n89ip import n89ip
from code.crawlProxies.kuaidaili import crawl_kuaidaili_proxies,crawl_kuaidaili_proxies1
from code.crawlProxies import goubanjia
from code.crawlProxies import seofangfa
from multiprocessing import Process
import platform
if platform.python_version()[0] == '3':
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser
from code.crawlProxies import crawl_proxies_conf
import time
import os
from code import etc
fp = os.path.join(etc.conf_path,'crawl_proxies.conf')
conf = ConfigParser()
conf.read(os.path.join(os.getcwd(),fp))
print(os.path.join(os.getcwd(),fp))
ilist = dir()
[ilist.remove(i) for i in ['os','crawl_proxies_conf','conf','ConfigParser', 'Process', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'fp', 'time']]
if 'all' in conf.sections():
    conf.set('all','name',str(ilist))
else:
    conf.add_section('all')
    conf.set('all', 'name', str(ilist))
with open(fp,'w')as f:
    conf.write(f)
crawl_proxies_conf.set_config(conf)
def crawlProxies():
    ps = []
    global fp,conf
    conf.read(fp)
    iliststr = conf.get('all','name')
    iliststr = iliststr.strip('[]').split(', ')
    ilist = [i.strip("'") for i in iliststr]
    for i in ilist:
        conf_sub = ConfigParser()
        sub_path = os.path.join(etc.conf_path,i+'.conf')
        conf_sub.read(sub_path)
        yn = conf_sub.get(i,'yn')
        if yn == 'True':
            last_time = conf_sub.getint(i,'last_time')
            interval_time = conf_sub.getint(i,'interval_time')
            now_time = int(time.time())
            if now_time - last_time > interval_time:
                ps.append(Process(target=globals()[i].crawl_proxies))
                conf_sub.set(i,'last_time',str(now_time))
                with open(sub_path,'w')as f:
                    conf_sub.write(f)
    print(len(ps))
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    return len(ps)
if __name__ == '__main__':
    crawlProxies()