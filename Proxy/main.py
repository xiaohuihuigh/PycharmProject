#coding:utf-8
# from code.verify_proxy_validity import *
import subprocess,time,sys
import multiprocessing
import os
import time
from Code import etc
import signal
import timeout_decorator
import platform
if platform.python_version()[0] == '3':
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

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

def set_timeout(num,callback=lambda :1):
    def wrap(func):
        def handle(signum,frame):
            raise RuntimeError
        def to_do(*args,**kwargs):
            try:
                signal.signal(signal.SIGALRM,handle)
                signal.alarm(num)
                r = func(*args,**kwargs)
                if r:
                    signal.alarm(0)
                return r
            except RuntimeError as e:
                callback()
        return to_do
    return wrap
@timeout_decorator.timeout(10)
def s_input(string):
    if string == None:
        return input()
    else:
        return input(string)
def ts_input(string = None,ex = None):
    try:
        t = s_input(string)
    except:
        t =  ex
    finally:
        if t == "":
            t = ex
        print(t)
        return t

def Proxies_init():
    # logconf_init()
    sys.stdout.write("\r If you want init the proxies process, input 'Y/y'; else wait 10 second\n")
    init_yn = ts_input()
    if not(init_yn == 'Y' or  init_yn == 'y'):
        return
    conf = ConfigParser()
    conf.read(os.path.join(etc.conf_path,'proxies.conf'))
    init_redis_host = ts_input("Input you redis host:[like 127.0.0.1]:",'127.0.0.1')
    init_redis_psw = ts_input("Input you redis password:",'zyh')
    init_redis_port = ts_input("Input you redis Port:[like 6379]",'6379')
    conf.set('redis','redis_host',init_redis_host)
    conf.set('redis','redis_psw',init_redis_psw)
    conf.set('redis','redis_port',init_redis_port)
    with open (os.path.join(etc.conf_path,'proxies.conf'),'w')as f:
        conf.write(f)

if __name__ == "__main__":

    Proxies_init()
    CMD = []
    pwd = etc.pwd
    loginfo.info(pwd)
    # CMD.append(os.path.join(pwd,'crawlProxies/kuaidaili/crawl_kuaidaili_proxies.py'))
    # CMD.append(os.path.join(pwd,'crawlProxies/kuaidaili/crawl_kuaidaili_proxies1.py'))
    CMD.append('Code.crawl_process')
    CMD.append('Code.alternate_process')
    CMD.append('Code.immediate_process')
    ps = []
    for i in CMD:
        p = multiprocessing.Process(target = Auto_Run,args=(TIME,i))
        ps.append(p)
    [p.start() for p in ps]
    [p.join() for p in ps]
    while True:
        time.sleep(1)

        sys.stdout.write("\r abc{}".format(time.time()))
        sys.stdout.flush()
