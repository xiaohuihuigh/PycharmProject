#coding:utf8
import Code.session
import time
from Code import etc
from lxml import etree

loginfo = etc.loginfo
logerr = etc.logerr
logipinfo = etc.logipinfo
verified_url = etc.verified_url
def verify_proxy(IP_info,test_url = etc.test_url):
    proxy = IP_info
    proxies = {
        'http': 'http://' + proxy['IP'] + ':' + proxy['port']
    }
    loginfo.info(proxy)
    # loginfo.info (proxies)
    try:
        loginfo.info("it wanner to get a url")

        rsp =Code.session.Session(proxies=proxies).get(url=test_url, timeout=10)

        loginfo.info(("it has get the url", etc.test_url))
        check_proxy_IP(rsp.text)

    except Exception as e:
        logerr.error(e)
        logerr.error('the proxy is error{}'.format(proxy['IP']))
        return False,None
    else:
        loginfo.info('the proxy could be use {}'.format(proxy['IP']))
        return True,int(time.time())

def check_proxy_IP(req):
    root = etree.HTML(req)
    proxy_type = "".join(root.xpath('//*[@id="result"]/strong/text()'))
    # word = re.findall(r'rel.*title.*href.*>(.*)</a></span>',req)
    proxy_info = "".join(root.xpath('//*[@id="result"]/text()'))
    logipinfo.info((proxy_type,proxy_info))

if __name__ == "__main__":
    proxy = {"IP":'125.25.55.46',"port":'1546'}
    verify_proxy(proxy)