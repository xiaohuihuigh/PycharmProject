#coding:utf-8
from Code import etc
import time
loginfo = etc.loginfo
logerr = etc.logerr
def get_a_proxy(anonymity=False):
    from Code import proxy_processing
    ap = proxy_processing.Proxy_processing(type='to_use', from_db=etc.immediate_db, to_db=etc.immediate_db)
    yn,proxy_info = ap.get_a_proxy()
    if yn:

        try:
            ap.push_or_discare(proxy_info)
            if proxy_info['anonymity'] == u'高匿名':
                loginfo.info(proxy_info)
                return {
                        'http':'http://'+proxy_info['IP']+':'+proxy_info['port']
                    }
            else:
                print(proxy_info['anonymity'])
                get_a_proxy()
        except Exception as e:
            logerr.error(e)
            return get_a_proxy()
    loginfo.info(None)
    return None
def check_proxy(type):
    from Code import proxy_processing
    ap = proxy_processing.Proxy_processing(type=type)
    yn,proxy_info = ap.get_a_proxy()
    if yn:
        try:
            ap.push_or_discare(proxy_info)
        except Exception as e:
            logerr.error(e)
if __name__ == "__main__":
    # for i in range(10):
    #     check_proxy('immediate')
    print (int(time.time()))
