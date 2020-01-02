import requests
from src.config import config


class Spider(requests.Session):
    def __init__(self, has_proxy=False, proxy=None, anonymity=True):
        super(Spider, self).__init__()
        if config.headers:
            self.headers = config.headers
        if has_proxy:
            if proxy:
                self.proxy = proxy
        self.anonymity = anonymity
        # else:
        #     self.proxies = getProxy.get_a_proxy(anonymity=anonymity)
    #
    # def get(self, url, **kwargs):
    #     r"""Sends a GET request. Returns :class:`Response` object.
    #
    #     :param url: URL for the new :class:`Request` object.
    #     :param **kwargs: Optional arguments that ``request`` takes.
    #     :rtype: requests.Response
    #     """
    #
    #     kwargs.setdefault('allow_redirects', True)
    #     threading.Thread(self.request())
    #     return self.request('GET', url, **kwargs)
