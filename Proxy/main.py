#coding:utf-8
from verify_proxy_validity import *
import subprocess,time,sys
import multiprocessing
import os
import time
import etc

loginfo = etc.loginfo
logerr = etc.logerr
TIME = 1
class Auto_Run():
    def __init__(self,sleelp_time,cmd):
        self.sleep_time = sleelp_time
        self.cmd = cmd
        self.ext = (cmd[-3:]).lower()
        self.p = None

        self.add_a = 0
        self.add_b = 0

        self.run()

        try:
            stime = time.time()
            while 1:
                etime = time.time()
                if etime - stime > 3540:
                    break
                time.sleep(sleelp_time *60)
                self.poll = self.p.poll()
                if self.poll is None:
                    loginfo.info("the process is runing")
                else:
                    loginfo.info("the process is end, and start to rerun the process")
                    self.run()
        except KeyboardInterrupt as e:
            logerr.error("check the Ctrl+c,and prepare to kill the process",e)
            self.p.kill()
    def run(self):
        if self.ext == ".py":
            loginfo.info('start ok!')
            self.add_a+=1
            self.add_b+=1
            self.p = subprocess.Popen(['python3','%s'%self.cmd],stdin=sys.stdin,stdout=sys.stdout,stderr=sys.stderr,shell=False)
        else:
            pass
if __name__ == "__main__":
    CMD = []
    pwd = os.path.dirname(os.path.realpath(__file__))
    loginfo.info(pwd)
    # CMD.append(os.path.join(pwd,'crawlProxies/kuaidaili/crawl_kuaidaili_proxies.py'))
    # CMD.append(os.path.join(pwd,'crawlProxies/kuaidaili/crawl_kuaidaili_proxies1.py'))
    CMD.append(os.path.join(pwd,'crawl_process.py'))
    CMD.append(os.path.join(pwd,'alternate_process.py'))
    CMD.append(os.path.join(pwd,'immediate_process.py'))
    loginfo.info(pwd)
    for i in CMD:
        p = multiprocessing.Process(target = Auto_Run,args=(TIME,i))
        p.start()
    p.join()

# multiprocessing.Process(Auto_Run(TIME,CMD2))
