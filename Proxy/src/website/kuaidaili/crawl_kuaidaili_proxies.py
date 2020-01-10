from src.spider.spider import Spider
from src.config import config
from src.proxy.proxy import Proxy
from src.proxy_io.proxy_io import ProxyIO


class KuAiDaiLi(Spider):

    def __init__(self, url=None):
        super(KuAiDaiLi, self).__init__()
        # self.pool = pool
        if url is None:
            self.url = config.s_kuaidaili_inha_url
        else:
            self.url = url
        self.dbIO = ProxyIO('file').IO
        self.insert = self.dbIO().set_proxy
        self.insert_s = self.dbIO().set_proxies
        self.crawl_proxies()

    def get_proxy_info(self, soup):
        IP_list = []
        proxy_soup_list = soup.select('tbody > tr')

        for proxy_soup in proxy_soup_list:
            proxy_dict = {}
            proxy_list = proxy_soup.findAll('td')
            proxy_dict["website"] = self.url
            for i in range(1, len(config.ip_attr_list)):
                proxy_dict[config.ip_attr_list[i]] = proxy_list[i - 1].text
            IP_list.append(Proxy.new_from_dict(proxy_dict))
            print(proxy_dict)
        return IP_list

    def crawl_proxies(self, a=1, b=50):
        for i in range(a, b):
            soup = self._get_html_to_soup(self.url.format(i))
            proxies = self.get_proxy_info(soup)
            print(proxies)
            self.insert_s(proxies)


if __name__ == "__main__":
    # kuai_dai_li = KuAiDaiLi(url=config.s_kuaidaili_intr_url)
    kuai_dai_li = KuAiDaiLi()