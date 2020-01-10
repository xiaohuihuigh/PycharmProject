# coding:utf-8
from src.config import config
import redis
import json
from src.proxy.proxy import Proxy
import random


# IPRedisIO 操作对象都为IP类的实例
class ProxyFileIO:
    def __init__(self):
        self.path = config.file_io_path

    def _read(self):
        with open(self.path, 'r')as f:
            for data in f:
                if data != "\n":
                    yield data

    def _read_add(self):
        with open(self.path, 'r+')as f:
            for data in f:
                if data != "\n":
                    yield data, f

    def _add(self, buf):
        try:
            with open(self.path, 'a')as f:
                f.write(buf + "\n")
        except:
            return False
        return True

    '''
    检测IP的是否存在于文件中，存在返回True并返回上次验证的时间，不存在返回False和None
    '''

    def check_proxy(self, proxy):
        # proxies_json = self._reads()
        for proxy_json in self._read():
            file_proxy = Proxy.new_from_json(proxy_json)
            if proxy.get_key() == file_proxy.get_key():
                return True, file_proxy.last_time
        return False, None

    '''
    插入数据成功返回True,没有成功插入返回False，暂时没有影响
    '''

    def set_proxy(self, proxy):
        try:
            yn, _ = self.check_proxy(proxy)
            if yn:
                return False

            self._add(proxy.to_json())
        except:
            return False
        else:
            return True

    '''
    set_proxies 插入多条数据  
    '''

    def set_proxies(self, proxies):
        for proxy in proxies:
            self.set_proxy(proxy)

    '''
    get_proxy 通过proxy_key返回一个Proxy的实例
    '''

    def get_proxy(self, proxy_key=None):
        if proxy_key is None:
            # proxies_json = self._reads()
            proxies_key = []
            proxies = []
            for proxy_json in self._read():
                proxy = Proxy.new_from_json(proxy_json)
                proxies.append(proxy)
                proxies_key.append(proxy.get_key())
            try:
                proxy_key = random.choice(proxies_key)
            except:
                return None
            for proxy in proxies:
                if proxy.get_key() == proxy_key:
                    return proxy
            return None
        else:
            # proxies_json = self._reads()
            for proxy_json in self._read():
                proxy = Proxy.new_from_json(proxy_json)
                if proxy_key == proxy.get_key():
                    return proxy
            return None

    '''
    从数据库中拿到n个可用信息
    返回一个列表，列表中的每一个元素为一个json格式的IP信息
    '''

    def get_proxies(self, n):
        # proxies_json = self._reads()
        proxies_key = []
        proxies = []
        for proxy_json in self._read():
            proxy = Proxy.new_from_json(proxy_json)
            proxies.append(proxy)
            proxies_key.append(proxy.get_key())

        result_proxies = []
        if len(proxies_key) < n:
            return proxies

        choice_proxies_key = random.sample(proxies_key, n)
        for proxy in proxies:
            if proxy.get_key() in choice_proxies_key:
                result_proxies.append(proxy)
        return result_proxies

    def delete(self, proxy):
        proxy_json = proxy.to_json()
        buf = []
        print(proxy_json)
        with open(self.path, 'r')as f:
            for line in f:
                print(line)
                if str(line.strip()) != str(proxy_json):
                    buf.append(line)
        with open(self.path, 'w')as f:
            f.writelines(buf)

    '''
    proxies_num 返回的数据库中有多少proxy
    '''

    def proxies_num(self):

        count = 0
        with open(self.path, 'r')as f:
            for _, _ in enumerate(f):
                count += 1
            print(count)


if __name__ == "__main__":
    t = Proxy(ip="123.123.344.213", port="12312")
    b = Proxy.new_from_json('{"ip":"224.225.33.221","port":"123"}')
    proxy_io = ProxyFileIO()
    proxy_io.set_proxy(t)
    proxy_io.set_proxy(b)
    print(proxy_io.get_proxy().get_key())
    # for proxy in proxy_io.get_proxies(1):
    #     proxy_io.delete(proxy)
