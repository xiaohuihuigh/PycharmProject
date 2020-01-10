# coding:utf-8

from src.proxy_io.proxy_redis_io import ProxyRedisIO
from src.proxy_io.proxy_file_io import ProxyFileIO


class ProxyIO:
    def __init__(self, io):
        if io == "redis":
            self.IO = ProxyRedisIO
        elif io == "file":
            self.IO = ProxyFileIO
