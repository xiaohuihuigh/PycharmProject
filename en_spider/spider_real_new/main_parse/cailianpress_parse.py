import re
import my_utils
import logging
import time
from six.moves.urllib.parse import urljoin
from base_parse import BaseParse
from lxml import etree
from items import Item

logger = logging.getLogger("parse")

#http://www.cailianpress.com/

class Cailianpress1(BaseParse):
	def _parse(self,raw_html):
		root = etree.HTML(raw_html)
		divs = root.xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[contains(@class,"jsx-3209043686")]')
		temp_timestamp = int(time.time() / 86400) * 86400
		for div in divs:
			item = Item()
			abstract = "".join(div.xpath(".//span[contains(@class,'jsx-3209043686')]/text()"))
			# print abstract
			if not abstract:
				print 'no abstract'
				continue
			title,abstract = my_utils.split_title_content(abstract)
			item.set('abstract',abstract)
			item.set('title',title)
			item.set('timestamp',time.time())
			roll_str = "".join(div.xpath(".//a//@href")).strip()
			roll_id = roll_str.split('/')[-1]
			nid = roll_id.split('&')[0]
			#nid = int('%s%s'%(temp_timestamp,roll_id))
			item.set('nid',nid)
			item.set('url','https://www.cls.cn/roll/'+str(nid))
			item.set('status',1)
			self._add_to_data(item)
			print 'status',item.get('status')
