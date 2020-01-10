#coding:utf-8
# from Code.verify_proxy_validity import *
import subprocess,time,sys
import multiprocessing
import os
import time
from Code import etc

loginfo = etc.loginfo
logerr = etc.logerr
TIME = 1
class Auto_Run():
    def __init__(self,sleelp_time,cmd):
        self.sleep_time = sleelp_time
        self.cmd = cmd
        # self.ext = (cmd[-3:]).lower()
        self.p = None
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
        # if self.ext == ".py":
        loginfo.info('start ok!')
        self.p = subprocess.Popen(['python3','-m','%s'%self.cmd],stdin=sys.stdin,stdout=sys.stdout,stderr=sys.stderr,shell=False,cwd=etc.parent)
        # else:
        #     pass
#if __name__ == "__main__":
def main():
    CMD = []
    pwd = etc.pwd
    loginfo.info(pwd)
    # CMD.append(os.path.join(pwd,'crawlProxies/kuaidaili/crawl_kuaidaili_proxies.py'))
    CMD.append('Code.crawl_process')
    CMD.append('Code.alternate_process')
    CMD.append('Code.immediate_process')
    ps = []
    for i in CMD:
        p = multiprocessing.Process(target = Auto_Run,args=(TIME,i))
        ps.append(p)
    [p.start() for p in ps]
    [p.join() for p in ps]

# multiprocessing.Process(Auto_Run(TIME,CMD2))
# from crawlProxies import crawl_proxies_conf
# crawl_proxies_conf.test()
