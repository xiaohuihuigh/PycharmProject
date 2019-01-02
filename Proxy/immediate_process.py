#coding:utf-8
from proxy_processing import Proxy_processing
import etc
import time

def immediate_process():
    ap = Proxy_processing(type='immediate',from_db=etc.alternate_db,to_db=etc.immediate_db)
    while 1:
        if ap.should_add_to_db():
            print('in the immediate_process')
            for i in range(etc.immediate_llen):
                try:
                    tf,IP_info=ap.get_a_proxy()
                    print(tf,IP_info)
                    if tf:
                        ap.push_or_discare(IP_info)
                        print('ab')
                    else:
                        time.sleep(10)
                except Exception as e:
                    print(e)
                    continue
        else:
            time.sleep(etc.immediate_sleep_time)
if __name__ == "__main__":
    immediate_process()
