import logging
import gevent.monkey
gevent.monkey.patch_all()
import gevent
from gevent.pool import Pool

import time
from datetime import datetime
import random
from settings import *

from main_request.get_request import Request

from main_parse.get_parse import Parse
from main_parse.content_parse import content_parse
logger = logging.getLogger('spider')

class Spider(object):
    def __init__(self):
        self._pool = Pool(CONCURRENT_ITEMS)
        self._parse = Parse()

        self._site = []
        self._data = []
        self._site_index = 0
        self._data_index = 0
        self._item_count = 0
        self._request_count = 0
        self._request = Request()
        CUR = CON.cursor()
        CUR.execute("select sid,re_url,url,source,weight,pbes,main_class,parse_func,status from spider_site "
                    "where status > 0 order by weight desc")
        self._site_argv = {}
        self._site_time = {}
        for sid,re_url,url,source,weight,pbes,main_class,parse_func,status in CUR.fetchall():
            self._site_argv[sid] = (re_url,url,source,weight,pbes,main_class,parse_func)
            self._site_time[sid] = 0
            print self._site_argv[sid]
        CUR.close()
        #self._other_list = (('http://data.eastmoney.com/datacenter_V3/Chart/cjsj/weeklystockaccountsnew.ashx?r=0.659568071773031&isxml=false',"investor_user_parse"))
        self._other_data = []
        logger.debug(self._site_time.keys())
    def _run(self,sid):
        logger.debug(sid)
        data = []
        re_url, url, source, weight, pbes, main_class, parse_func = self._site_argv[sid]
        logger.debug('in')
        # '''what is pbes'''
        # if pbes:
        #     lists = [int(tmp) for tmp in pbes.split(',')]
        #     if random.randint(0,100) < lists[0]:
        #         return
        #     if self._second < lists[1] or self._second > lists[2]:
        #         return
        request = self._request.get_class(sid = sid)
        title = self._parse.get_class(sid)
        step = time.time() - self._site_time[sid]
        if step < self._step:
            gevent.sleep(self._step - step)
        while request.COUNTS > CONCURRENT_PER_REQUESTS:
            gevent.sleep(0)
        html = None
        with gevent.Timeout(30,False) as timeout:
            timestamp = time.time()
            html = request.run(url)
            self._site_time[sid] = (time.time()+timestamp)/2
        if html:
            logger.debug("have html")
            data = title.run(html,sid,url=source,weight=weight)
            if data:
                logger.debug("sid: %s, new data length:%s,url:%s"%(sid,len(data),source))
                print ("hasdata")

            else:
                logger.debug("%s not data"%url)
                print ("nodata")
        else:
            logger.error("sid :%s ,url :%s html is empty"%(sid,source))
        self._site.append((sid,data))
        print self._site
    def _update(self,item):
        print 'in here '
        print item.get('status')
        if item.get('status') >0:
            request = self._request.get_class(sid=item.get('sid'),mode=True)
            while request.COUNTS > CONCURRENT_PER_REQUESTS:
                gevent.sleep(0)
            html = None
            with gevent.Timeout(30,False) as timeout:
                html = request.run(url=item.get('url'),num = 3)
            if html:
                # print item.get('url'),'yes',html.text
                print 'self._site_argv[item.get(sid)][-1]',self._site_argv[item.get('sid')][-1]
                content_parse(self._site_argv[item.get('sid')][-1],html,item)
        # print item.get('content')
        # print item.get('title')
        print item.gets()
        self._data.append(item)
    def _other(self,argv):
        request = self._request.get_class(sid=0)
    def run(self):
        timestamp = time.time()
        self._second = int(timestamp + 28800) % 86400

        stoptime = int (timestamp/3600)*3600+3570
        self._step = 10 if timestamp % 86400 < 28800 else 60
        self._pipetime = timestamp +30
        logger.debug(self._site_time)
        for sid in self._site_time:
            print 'sid',sid
            self._pool.add(gevent.spawn(self._run,sid))
        logger.debug('after pool add')
        print('after pool add run')
        print len(self._site)
        self._pool.join()
        # while(1):
        #     time.sleep(3)
        #     for item in self._site[0][1]:
        #         self._update(item)
        #         # print item

        GET_CONTENT = True
        while GET_CONTENT and timestamp < stoptime:
            timestamp = time.time()
            time.sleep(1)
            self._second = int(timestamp + 28800) % 86400
            print("sitelen",len(self._site))
            if len(self._site) > self._site_index:
                for item in self._site[self._site_index][1]:
                    self._pool.add(gevent.spawn(self._update,item))
                logger.debug('after pool run')
                self._pool.add(gevent.spawn(self._run,self._site[self._site_index][0]))
                logger.debug('after pool run1')
                self._site_index +=1
            len_data = len(self._data)
            timestamp = time.time()
        self._pool.join()
