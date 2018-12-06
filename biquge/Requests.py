

import requests
import json

class Requests(requests):
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    def get(self,url,header=header,timeout=10):
        super(Requests,self).get(url,header = header,timeout=timeout)
