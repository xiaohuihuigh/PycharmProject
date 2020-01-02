from src.spider.spider import Spider
from bs4 import BeautifulSoup as bf
# from Code import etc, proxy_io
from src.pool.pool import pool
from src.config import config


class KuAiDaiLi(Spider):

    def __init__(self):
        super(KuAiDaiLi, self).__init__()
        self.pool = pool
        self.url = config.s_kuaidaili_inha_url

    def _get_html_to_soup(self, url):
        response = self.get(url)
        soup = bf(response.text, 'html.parser')
        return soup

    def  get_proxies_info(self, soup):
        proxies_info_list = []
        proxy_soup_list = soup.select('tbody > tr')

        for proxy_soup in proxy_soup_list:
            proxy_info_dict = {}
            proxy_info_list = proxy_soup.findAll('td')
            for i in range(len(config.ip_attr_list)):
                proxy_info_dict[config.ip_attr_list[i]] = proxy_info_list[i].text
            proxies_info_list.append(proxy_info_dict)
            print(proxies_info_list)
        # return proxies_info_list

    def crawl_proxies(self, a=1, b=2):
        for i in range(a, b):

            # soup = self._get_html_to_soup(self.url.format(i))
            self.pool.apply(self._get_html_to_soup, (self.url.format(i),))
            # self.get_proxies_info(soup)
            # pool.apply(self.get_proxies_info, (soup,))
            # proxy_db = proxy_io.ProxiesIO(db=config.crawl_db)
            # for proxy in proxies_list:
            #     proxy_db.insert_proxy(proxy)


if __name__ == "__main__":
    kuai_dai_li = KuAiDaiLi()
    kuai_dai_li.crawl_proxies()
