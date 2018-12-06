import subprocess,time,sys
import multiprocessing
TIME = 1
CMD = ['/home/zyh/PycharmProjects/biquge/down_load_one_page.py']

class Auto_Run():
    def __init__(self,sleelp_time,cmd):
        self.sleep_time = sleelp_time
        self.cmd = cmd
        self.ext = (cmd[-3:]).lower()
        self.p = None

    def auto_run(self):
        self.run()
        print('true')
        try:
            while 1:
                time.sleep(self.sleep_time *30)
                self.poll = self.p.poll()
                if self.poll is None:
                    print ("the process is runing")
                else:
                    print ("the process is end, and start to rerun the process")
                    self.run()
        except KeyboardInterrupt as e:
            print ("check the Ctrl+c,and prepare to kill the process")
            self.p.kill()
    def run(self):
        if self.ext == ".py":
            print ('start ok!')
            self.p = subprocess.Popen(['python','%s'%self.cmd],stdin=sys.stdin,stdout=sys.stdout,stderr=sys.stderr,shell=False)
        else:
            pass

s =Auto_Run(TIME,CMD[0])
p = multiprocessing.Process(target = s.auto_run())

print('ues')
p.start()
p.join()

# multiprocessing.Process(Auto_Run(TIME,CMD2))
