# coding:utf-8
from src.config import config
import redis
import json
from src.proxy.proxy import Proxy


# IPRedisIO 操作对象都为IP类的实例
class ProxyRedisIO(redis.Redis):
    def __init__(self, host=config.redis_host, port=config.redis_port, password=config.redis_psw, db=config.redis_db):
        super(ProxyRedisIO, self).__init__(host=host, port=port, password=password, db=db)
        # 可以在初始化的时候创建如果没有list的话？？？
        # 具体看怎么存的。。。

    '''
    检测IP的是否存在于数据库中，存在返回True并返回上次验证的时间，不存在返回False和None
    '''

    def check_proxy(self, proxy):
        proxy_key = proxy.get_key()
        if self.check_proxy_by_key(proxy_key):
            return True, self.get_proxy(proxy_key).last_c_time
        else:
            return False, None


    '''
    根据keys检测IP是否存在与数据库中，存在返回True，不存在返回False
    '''

    def check_proxy_by_key(self, ip_key):
        if self.exists(ip_key):
            return True
        else:
            return False

    '''
    delete_proxy 删除一个proxy
    '''
    def delete_proxy(self, proxy):
        self.delete(proxy.get_key())

    '''
    插入数据成功返回True,没有成功插入返回False，暂时没有影响
    '''

    def set_proxy(self, proxy):
        proxy_key = proxy.get_key()
        try:
            if self.check_proxy_by_key(proxy_key):
                proxy_in_db = self.get_proxy(proxy_key)
                if proxy.last_time < proxy_in_db.last_time:
                    return

            self.set(proxy_key, json.dumps(proxy))
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
            proxy_key = self.randomkey()
            self.delete(proxy_key)
            if proxy_key is None:
                return None
            return self.get_proxy(proxy_key)
        else:
            return Proxy.new_from_json(self.get(proxy_key))
    '''
    从数据库中拿到n个可用信息
    返回一个列表，列表中的每一个元素为一个json格式的IP信息
    '''

    def get_proxies(self, n):
        proxies = []
        for i in range(n):
            proxies.append(self.get_proxy())
        return proxies

    '''
    proxies_num 返回的数据库中有多少proxy
    '''

    def proxies_num(self):
        return self.dbsize()

    @staticmethod
    def byte2str(b):
        return b.decode('utf8') if isinstance(b, bytes) else b


if __name__ == "__main__":
    proxy_io = ProxyRedisIO()
    print(proxy_io.get_proxy())
