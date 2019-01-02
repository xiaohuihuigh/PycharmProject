#coding:utf-8
from proxy_processing import Proxy_processing
import etc
import time
def alternate_process():
    ap = Proxy_processing(type='alternate',from_db=etc.crawl_db,to_db=etc.alternate_db)
    while 1:
        if ap.should_add_to_db():

            print('test alternate')
            for i in range(etc.alternate_llen):
                try:
                    tf,IP_info=ap.get_a_proxy()
                    if tf:
                        print('in alternate mode get a proxy',IP_info)
                        ap.push_or_discare(IP_info)
                        print('push, or discare')
                    else:
                        time.sleep(10)
                except Exception as e:
                    print(e)
                    print ('*******************')
                    # time.sleep(10)
                    continue
                else:
                    pass
                    # time.sleep(10)

        else:
            time.sleep(etc.alternate_sleep_time)

if __name__ == "__main__":
    alternate_process()
