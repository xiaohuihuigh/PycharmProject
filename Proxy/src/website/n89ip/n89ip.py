from Code.session import Session
import time
from src.spider.spider import Spider
from src.proxy_io.proxy_io import ProxyIO
from lxml import etree
from src.config import config
# loginfo = etc.loginfo


class N89IP(Spider):
    def __init__(self, url=None):
        super(N89IP, self).__init__()
        if url is None:
            self.url = config.s_kuaidaili_inha_url
        else:
            self.url = url
        self.dbIO = ProxyIO('file').IO
        self.insert = self.dbIO().set_proxy
        self.insert_s = self.dbIO().set_proxies
        self.crawl_proxies()

    def get_html_to_tree(self, url):
        response = self.get(url)
        root = etree.HTML(response.text)
        return root

    def get_proxies_info(self, root):
        proxies_info_list = []
        proxy_root_list = root.xpath('//tbody/tr')

        for proxy_root in proxy_root_list:
            proxy_info_dict = {}
            proxy_info_dict['website'] = self.url
            proxy_info_list = proxy_root.xpath('.//td/text()')
            info_list = ['IP','port','locate']#,'anonymity','ptype','locate','resspeed']
            proxy_info_dict['IP'] = proxy_info_list[0].strip()
            proxy_info_dict['port'] = proxy_info_list[1].strip()
            proxy_info_dict['locate'] = proxy_info_list[2].strip()+proxy_info_list[3].strip()
            proxy_info_dict['ptype'] = 'http'
            proxy_info_dict['anonymity'] = 'unknow'
            proxy_info_dict['resspeed'] = '0'
            print(proxy_info_dict)
            proxies_info_list.append(proxy_info_dict)
        return proxies_info_list

    def crawl_proxies(self):
        # loginfo.info('crawl proxies in n89ip')
        for i in range(1,20):
            time.sleep(3)
            root = self.get_html_to_tree(config.s_89ip_url.format(i))
            proxies = self.get_proxies_info(root)
            # self.insert_s(proxies)


#网站不能用了？？
if __name__ == "__main__":
    N89IP()