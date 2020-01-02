# coding:utf-8
from src.config.config import ip_attr_list


class IP:

    def __init__(self, *args):
        attr_list = ip_attr_list
        if len(args) == 1:
            ip_info = IP.json2map(args[0])
            for i in range(len(attr_list)):
                self.__setattr__(attr_list[i], ip_info[attr_list[i]])
        elif len(args) == 8:
            for i in range(len(attr_list)):
                self.__setattr__(attr_list[i], args[attr_list[i]])
        else:
            for i in range(len(attr_list)):
                self.__setattr__(attr_list[i], None)

    # pass
    @classmethod
    def json2map(cls, json_ip_info):
        ip_info = json_ip_info
        return cls(ip_info)

    # ToJson 将Ip类型的对象转换成Json格式
    def to_json(self):
        pass
