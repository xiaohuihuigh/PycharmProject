import requests
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/opt/phantomjs/bin/phantomjs')

url = 'http://ip.zdaye.com/dayProxy/ip/208741.html'
# url = 'www.baidu.com'
head = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'acw_tc=76b20f7115464079168466292e7fd0d34c0f58399805e23eba9a7c4970ae02; ASPSESSIONIDCASQCRCT=ECFFBDCCMABAIBJKKGKGJIHI; __51cke__=; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1546407921; acw_sc__v3=2866D37C05AB8A6703E3752CD0F72C1675CF1C67; acw_sc__v2=NWMyYzUzZjZlZTA0MzRlNzc0MzZiMWM4YmU1OWEzOWJiOTA1YjI3MQ==; ASPSESSIONIDACTQCQDS=DLONBKCCMBDHLCELPKAFBIEO; __tins__16949115=%7B%22sid%22%3A%201546409786708%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201546412880164%7D; __51laig__=56; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1546411081',
            'Host': 'ip.zdaye.com',
            'Referer': 'http://ip.zdaye.com/dayProxy/2019/1/1.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
driver.get(url)
# with open('test.html','a')as f:
#     f.write(driver.page_source.decode('utf-8').encode('utf-8'))
print driver.page_source