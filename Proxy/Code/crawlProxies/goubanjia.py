#coding:utf-8
from Code.session import Session
from lxml import etree
from Code import etc,proxy_io
loginfo = etc.loginfo
def get_html_to_tree(url):
    response = Session().get(url)
    root = etree.HTML(response.text)
    return root

def get_proxies_info(root):
    proxies_info_list = []
    proxy_root_list = root.xpath('//*[@id="services"]//tbody/tr')
    # print len(proxy_root_list)
    for proxy_root in proxy_root_list:
        # print len(proxy_root.xpath('./td'))

        proxy_info_dict = {}
        proxy_info_list = proxy_root.xpath('./td')
        info_list = ['IP:port','anonymity','ptype','locate','yunyingshang','resspeed']#,'anonymity','ptype','locate','resspeed']
        proxy_list =  ["".join(i.xpath("./span/text() | ./text() | ./div/text() | ./a/text()")).strip() for i in proxy_info_list]
        # print proxy_list

        proxy_info_dict['IP'] = proxy_list[0].split(':')[0]
        proxy_info_dict['port'] = proxy_list[0].split(':')[1]
        proxy_info_dict['resspeed'] = proxy_list[5]
        proxy_info_dict['locate'] = "".join(proxy_list[3].split())
        proxy_info_dict['ptype'] = proxy_list[2]
        proxy_info_dict['anonymity'] = proxy_list[1]
        # print proxy_list[3].split()
        # print proxy_info_dict
        # print proxy_info_dict['IP'],proxy_info_dict['port'],proxy_info_dict['resspeed'] ,proxy_info_dict['locate'],\
        # proxy_info_dict['ptype'] , proxy_info_dict['anonymity']
        proxies_info_list.append(proxy_info_dict)
    return proxies_info_list
def crawl_proxies():
    loginfo.info('crawl proxies in goubanjia')
    print ('crawl proxies in goubanjia')
    root = get_html_to_tree(etc.goubanjia_url)
    proxies_list = get_proxies_info(root)
    proxy_db = proxy_io.ProxiesIO(db = etc.crawl_db)
    for proxy in proxies_list:
        # verify_proxy_validity.verify_proxy(proxy)
        proxy_db.insert_proxy(proxy)

if __name__ == "__main__":
    crawl_proxies()