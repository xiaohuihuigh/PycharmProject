#coding:utf-8
import  proxy_processing
import etc
import time
def get_a_proxy():
    ap = proxy_processing.Proxy_processing(type='to_use', from_db=etc.immediate_db, to_db=etc.immediate_db)
    yn,proxy_info = ap.get_a_proxy()
    if yn:
        try:
            ap.push_or_discare(proxy_info)
            print(proxy_info)
            return {
                    'http':'http://'+proxy_info['IP']+':'+proxy_info['port']
                }
        except Exception as e:
            print(e)
            return get_a_proxy()
    print(None)
    return None
