#coding:utf-8
import subprocess,time,sys
import multiprocessing
TIME = 1
CMD = ['/home/zyh/PycharmProjects/aisinei/main.py','/home/zyh/PycharmProjects/aisinei/teding.py']

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
            while 1:
                time.sleep(sleelp_time *60)
                self.poll = self.p.poll()
                if self.poll is None:
                    print "the process is runing"
                else:
                    print "the process is end, and start to rerun the process"
                    self.run()
        except KeyboardInterrupt as e:
            print "check the Ctrl+c,and prepare to kill the process"
            self.p.kill()
    def run(self):
        if self.ext == ".py":
            print 'start ok!'
            self.add_a+=1
            self.add_b+=1
            self.p = subprocess.Popen(['python','%s'%self.cmd],stdin=sys.stdin,stdout=sys.stdout,stderr=sys.stderr,shell=False)
        else:
            pass
for i in range(2):
    p = multiprocessing.Process(target = Auto_Run,args=(TIME,CMD[i]))
    p.start()
p.join()

# multiprocessing.Process(Auto_Run(TIME,CMD2))
