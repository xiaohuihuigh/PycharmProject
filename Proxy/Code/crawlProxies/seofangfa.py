#coding:utf-8
from Code.session import Session
from lxml import etree
from Code import etc, proxy_io
loginfo = etc.loginfo
def get_html_to_tree(url):
    response = Session().get(url)
    root = etree.HTML(response.text)
    return root

def get_proxies_info(root):
    proxies_info_list = []
    proxy_root_list = root.xpath('*//tbody[1]/tr')

    for proxy_root in proxy_root_list:
        proxy_info_dict = {}
        proxy_info_list = proxy_root.xpath('.//td/text()')
        info_list = ['IP','port','resspeed','locate']#,'anonymity','ptype','locate','resspeed']
        proxy_info_dict['IP'] = proxy_info_list[0].strip()
        proxy_info_dict['port'] = proxy_info_list[1].strip()
        proxy_info_dict['resspeed'] = proxy_info_list[2].strip()
        proxy_info_dict['locate'] = proxy_info_list[3].strip()
        proxy_info_dict['ptype'] = 'http'
        proxy_info_dict['anonymity'] = 'unknow'

        proxies_info_list.append(proxy_info_dict)
    return proxies_info_list
def crawl_proxies():
    loginfo.info('crawl proxies in seofangfa')
    root = get_html_to_tree(etc.seofangfa_url)
    proxies_list = get_proxies_info(root)
    proxy_db = proxy_io.ProxiesIO(db = etc.crawl_db)
    for proxy in proxies_list:
        # verify_proxy_validity.verify_proxy(proxy)
        proxy_db.insert_proxy(proxy)
if __name__ == "__main__":
    crawl_proxies()