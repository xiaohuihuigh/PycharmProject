#coding:utf-8
from code import proxy_processing,etc
import time
from multiprocessing import Process

loginfo = etc.loginfo
logerr = etc.logerr

def immediate_process():
    ap = proxy_processing.Proxy_processing(type='immediate',from_db=etc.alternate_db,to_db=etc.immediate_db)
    s_time = time.time()
    while time.time() - s_time < 3600:
        if ap.should_add_to_db():
            loginfo.info('in the immediate_process')
            for i in range(etc.immediate_llen):
                try:
                    tf,IP_info=ap.get_a_proxy()
                    loginfo.info((tf,IP_info))
                    if tf:
                        ap.push_or_discare(IP_info)
                        loginfo.info('ab')
                    else:
                        time.sleep(10)
                except Exception as e:
                    logerr.error(e)
                    time.sleep(5)
                    continue
        else:
            time.sleep(etc.immediate_sleep_time)
def immediate_db_rool():
    ap = proxy_processing.Proxy_processing(type='immediate',from_db=etc.immediate_db)
    s_time = time.time()
    multiple_hits = 0
    while time.time() - s_time < 3600:
        tf,proxy_info = ap.get_a_proxy()
        if tf:
            if ap.push_or_discare(proxy_info):
                multiple_hits = 0
            else:
                multiple_hits += 1
        else:
            time.sleep(etc.alternate_effective_time)
        if multiple_hits > ap.from_redis.check_len_db():
            time.sleep(etc.alternate_effective_time/2)
        time.sleep(2)

if __name__ == "__main__":
    p1 = Process(target=immediate_process())
    p2 = Process(target=immediate_db_rool())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
