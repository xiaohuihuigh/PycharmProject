import session
from bs4 import BeautifulSoup as bf
import time
import json
from lxml import etree
import etc
import proxy_io
def get_html_to_tree(url):
    response = session.Session().get(url)
    root = etree.HTML(response.text)
    return root

def get_proxies_info(root):
    proxies_info_list = []
    proxy_root_list = root.xpath('//tbody/tr')

    for proxy_root in proxy_root_list:
        proxy_info_dict = {}
        proxy_info_list = proxy_root.xpath('.//td/text()')
        info_list = ['IP','port','locate']#,'anonymity','ptype','locate','resspeed']
        proxy_info_dict['IP'] = proxy_info_list[0].strip()
        proxy_info_dict['port'] = proxy_info_list[1].strip()
        proxy_info_dict['locate'] = proxy_info_list[2].strip()+proxy_info_list[3].strip()
        proxy_info_dict['ptype'] = 'http'
        proxy_info_dict['anonymity'] = 'unknow'
        proxy_info_dict['resspeed'] = '0'

        proxies_info_list.append(proxy_info_dict)
    return proxies_info_list
def crawl_proxies():
    for i in range(1,20):
        time.sleep(3)
        root = get_html_to_tree(etc.s_89ip_url.format(i))
        proxies_list = get_proxies_info(root)
        proxy_db = proxy_io.ProxiesIO(db = etc.crawl_db)
        for proxy in proxies_list:
            proxy_db.insert_proxy(proxy)
if __name__ == "__main__":
    crawl_proxies()