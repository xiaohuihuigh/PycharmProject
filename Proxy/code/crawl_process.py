#coding:utf-8
from code import proxy_processing, etc
import time
from code.crawlProxies import crawl_proxies
loginfo = etc.loginfo
logerr = etc.logerr
def crawl_process():
    ap = proxy_processing.Proxy_processing(type='crawl')
    s_time = time.time()
    while time.time() - s_time < 3600:
        if ap.should_add_to_db():
            loginfo.info('add to crawl')
            try:
                if not crawl_proxies.crawlProxies():
                    time.sleep(etc.crawl_sleep_time)
            except Exception as e:
                print(e)
                time.sleep(10)
                logerr.error(e)
        else:
            time.sleep(etc.crawl_sleep_time)

if __name__ == "__main__":
    crawl_process()
