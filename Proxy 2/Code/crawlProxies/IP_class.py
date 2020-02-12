#coding:utf-8


class IP():

    def __init__(self):
        self.ip=None
        self.port=None
        self.resspeed=None
        self.locate=None
        self.ptype=None
        self.anonymity=None
        self.last_c_time=None
    '''
    
    将字典类型表示的ip转换成对象
    
    返回结果为一个包含ip对象的list列表或None
    
    '''
    @classmethod
    def list_to_ip(self,list_or_dict):
        lists = []
        if type(list_or_dict) is dict or list:
            if type(list_or_dict) is dict:
                lists.append(list_or_dict)
            else:
                lists = list_or_dict
            resp = []
            for ip_dict in lists:
                t = IP()
                for key,value in ip_dict.items():
                    setattr(t,key,value)
                resp.append(t)
            return resp
        else:
            return None

if __name__ == "__main__":
    lists = {'ip':'asdf'}
    # for key in lists:
    #     print key,lists[key]
    print IP.list_to_ip(lists)