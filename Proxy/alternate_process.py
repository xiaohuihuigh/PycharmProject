#coding:utf-8
import proxy_processing
import etc
import time
from multiprocessing import Process
from crawlProxies import crawl_proxies
loginfo = etc.loginfo
logerr = etc.logerr
def alternate_process():
    ap = proxy_processing.Proxy_processing(type='alternate')
    s_time = time.time()
    while time.time() - s_time < 3600:
        if ap.should_add_to_db():
            loginfo.info('test alternate')
            for i in range(etc.alternate_llen):
                try:
                    tf,IP_info=ap.get_a_proxy()
                    if tf:
                        loginfo.info(('in alternate mode get a proxy',IP_info))
                        ap.push_or_discare(IP_info)
                        loginfo.info('push, or discare')
                    else:
                        if not crawl_proxies.crawlProxies():
                            time.sleep(10)
                            logerr.error('crawlproxies con`t had been used')
                        else:
                            loginfo.info('run mimvp once')
                except Exception as e:
                    logerr.error(e)
                    logerr.error ('*******************')
                    time.sleep(5)
                    continue
                else:
                    pass
                    # time.sleep(10)

        else:
            time.sleep(etc.alternate_sleep_time)
def alternate_db_rool():
    ap = proxy_processing.Proxy_processing(type='alternate',from_db=etc.alternate_db)
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
    p1 = Process(target=alternate_process)
    # p2 = Process(target=alternate_db_rool)
    p1.start()
    # p2.start()
    p1.join()
    # p2.join()
