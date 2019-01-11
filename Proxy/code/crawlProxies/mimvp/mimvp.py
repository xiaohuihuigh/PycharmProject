from code.session import Session
import time
from lxml import etree
from code import etc,proxy_io
import json
loginfo = etc.loginfo
def get_html_to_tree(url):
    response = Session().get(url)
    root = etree.HTML(response.text)
    return root
def get_html_to_json(url):
    response = Session().get(url)
    j_dict = json.loads(response.text)
    return j_dict
def get_proxies_info(j_dict):
    proxies_info_list = []
    proxy_dict_list = j_dict['result']

    for proxy_dict in proxy_dict_list:
        proxy_info_dict = {}
        info_list = ['IP','port','locate']#,'anonymity','ptype','locate','resspeed']
        proxy_info_dict['IP'] = proxy_dict['ip:port'].split(":")[0]
        proxy_info_dict['port'] = proxy_dict['ip:port'].split(":")[1]
        proxy_info_dict['locate'] = proxy_dict['country']
        proxy_info_dict['ptype'] = proxy_dict['http_type']
        proxy_info_dict['anonymity'] = proxy_dict['anonymous']
        proxy_info_dict['resspeed'] = proxy_dict['transfer_time']
        proxies_info_list.append(proxy_info_dict)
    return proxies_info_list
def crawl_proxies_loop():
    proxy_db = proxy_io.ProxiesIO(db=etc.crawl_db)
    while True:
        loginfo.info('crawl proxies in mimvp in loop')
        s_time = time.time()
        j_dict = get_html_to_json(etc.mimvp_api_url)
        proxies_list = get_proxies_info(j_dict)
        for proxy in proxies_list:
            proxy_db.insert_proxy(proxy)
        time.sleep(0 if time.time() - s_time > 60 else 60 - (time.time() - s_time))
def crawl_proxies():
    loginfo.info('crawl proxies in mimvp not in loop')
    proxy_db = proxy_io.ProxiesIO(db=etc.crawl_db)
    j_dict = get_html_to_json(etc.mimvp_api_url)
    proxies_list = get_proxies_info(j_dict)
    for proxy in proxies_list:
        proxy_db.insert_proxy(proxy)
    loginfo.info('crawl proxies in mimvp not in loop end')
    if len(proxies_list) < 20:
        return False
    return True
if __name__ == "__main__":
    crawl_proxies()