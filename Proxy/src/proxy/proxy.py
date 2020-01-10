# coding:utf-8
import json


class Proxy:
    def __init__(self, ip, port,
                 anonymity=None, p_type=None,
                 locate=None, res_speed=None,
                 website=None, last_time=None):
        self.ip = ip
        self.port = port
        self.anonymity = anonymity
        self.p_type = p_type
        self.locate = locate
        self.res_speed = res_speed
        self.last_time = last_time
        self.website = website

    '''
    new_from_json 从json格式生成Proxy实例
    '''
    @classmethod
    def new_from_json(cls, raw_body):
        proxy_dict = json.loads(raw_body.strip())
        if 'anonymity' not in proxy_dict:
            proxy_dict['anonymity'] = None
        if 'p_type' not in proxy_dict:
            proxy_dict['p_type'] = None
        if 'locate' not in proxy_dict:
            proxy_dict['locate'] = None
        if 'res_speed' not in proxy_dict:
            proxy_dict['res_speed'] = None
        if 'website' not in proxy_dict:
            proxy_dict['website'] = None
        if 'last_time' not in proxy_dict:
            proxy_dict['last_time'] = None

        return cls(proxy_dict["ip"], proxy_dict["port"],
                   proxy_dict['anonymity'], proxy_dict['p_type'],
                   proxy_dict['locate'], proxy_dict['res_speed'],
                   proxy_dict['website'], proxy_dict['last_time'])

    @classmethod
    def new_from_dict(cls, proxy_dict):
        return cls(proxy_dict["ip"], proxy_dict["port"],
                   proxy_dict['anonymity'], proxy_dict['p_type'],
                   proxy_dict['locate'], proxy_dict['res_speed'],
                   proxy_dict['website'], proxy_dict['last_time'])
    # get_key 根据ip和port生成key
    # ip类型 123:123:123:123 255
    # port类型 1234 65536
    # key 是两者的结合
    def get_key(self):
        result = 0

        for i in self.ip.split("."):
            print(int(i))
            result *= 1000
            result += int(i)
        result *= 1e5
        print(result)
        return result + int(self.port)

    def to_json(self):
        proxy_dict = {'ip': self.ip,
                      'port': self.port,
                      'anonymity': self.anonymity,
                      'p_type': self.p_type,
                      'locate': self.locate,
                      'res_speed': self.res_speed,
                      'website': self.website,
                      'last_time': self.last_time}
        return json.dumps(proxy_dict)


if __name__ == "__main__":
    t = Proxy(ip="asdf", port="adfdf")
    b = Proxy.new_from_json('{"ip":"afff","port":"awdfas"}')
    print(t.ip, t.last_time, b.ip)
