#coding:utf-8
from Code import etc
import redis
import json
import re
loginfo = etc.loginfo
logerr = etc.logerr
# redis_h.lpush()
class ProxiesIO(redis.Redis):
    def __init__(self,host=etc.redis_host,port = etc.redis_port,password=etc.redis_psw,db=etc.crawl_db):
        super(ProxiesIO,self).__init__(host=host,port=port,password=password,db=db)
        #可以在初始化的时候创建如果没有list的话？？？
        #具体看怎么存的。。。
    @staticmethod
    def get_IPkey(IP_info):
        IP = IP_info['IP']
        port = IP_info['port']
        ip_list = IP.split('.')
        proxy = IP+port
        key = "".join(re.findall(r'\d',IP+port))
        return key
    '''
    暂时还不知道是干嘛的。。。
    '''
    # def create_list(self, listname, *values):
    #     self.lpush(listname, *values)


    '''
    检测IP的是否存在于数据库中，存在返回True并返回上次验证的时间，不存在返回False和None
    '''
    def check_proxy_in(self,IP_info):
        IPkey = self.get_IPkey(IP_info)
        if self.exists(IPkey):
            IP_info = self.get(IPkey)
            IP_info = json.loads(IP_info)
            return True,IP_info['last_c_time']
        else:
            return False,None
    '''
    根据keys检测IP是否存在与数据库中，存在返回True，不存在返回False
    '''
    def check_proxy_with_key(self,IPkey):
        if self.exists(IPkey):
            return True
        else:
            return False
    '''
    插入数据成功返回Ture，没有成功插入返回False，暂时没有影响
    '''
    def insert_proxy(self,IP_info):
        IPkey = self.get_IPkey(IP_info)
        try:
            if not self.check_proxy_with_key(IPkey):
                self.set(IPkey,json.dumps(IP_info))
                # print(IP_info['IP'],'is not in redis')
                loginfo.info((IP_info['IP'],':',IP_info['port']))
            # else:
                # print(IP_info['IP'], 'is in redis')
        except Exception as e:
            logerr.error('insert the proxy',IP_info,'false')
            return False
        else:
            return True
    '''
    从数据库中拿到一个可用的IP信息
    返回一条json格式的IP信息
    
    采用多线程的等待模式 blpop ，等待时间10s
    '''
    def pop_proxy(self):
        IPkey = self.randomkey()
        if IPkey == None:
            return None
        IP_info = self.get(IPkey)

        self.delete(IPkey)
        if IP_info:
            IP_info = json.loads(IP_info.decode('utf-8'))
            return IP_info
        return None
    # '''
    # 从数据库中拿到n个可用信息
    # 返回一个列表，列表中的每一个元素为一个json格式的IP信息
    # '''
    # def pop_n_proxies(self,n):
    #     proxies_list = []
    #     for i in range(n):
    #         proxies_list.append(self.pop_proxy())
    #     return proxies_list
    '''
    返回一个列表的长度
    '''
    def check_len_db(self):
        return self.dbsize()
    @staticmethod
    def byte2str(b):
        return b.decode('utf8') if isinstance(b, bytes) else b

