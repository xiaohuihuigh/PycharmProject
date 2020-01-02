import requests
from Code import etc
import to_use


def Session(has_proxy=False, proxies=None, anonymity=True):
    s = requests.Session()
    if etc.headers:
        s.headers = etc.headers
    if proxies:
        s.proxies = proxies
    elif has_proxy:
        s.proxies = to_use.get_a_proxy(anonymity=anonymity)
    return s
