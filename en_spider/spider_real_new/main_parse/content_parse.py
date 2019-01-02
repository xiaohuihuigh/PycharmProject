# -*- encoding:utf-8 -*-
#! /usr/bin/python
# 内容解析模块


import logging
import re
import my_utils
from lxml.etree import HTML
#from breadability.readable import Article
#from breadability.readable import Article
_func_host = {"aastocks1": ("www.aastocks.com",),
              "cailianpress1": ("www.cailianpress.com",),
              "ccstock1": ("www.ccstock.cn", "www.zqrb.cn"),
              "cfi1": ("cfi.net.cn", "www.cfi.net.cn"),
              "cfi2": ("stock.cfi.cn", ),
              "china1": ("finance.china.com.cn",), "china2": ("finance.china.com.cn",),
              "cnfol1": ("news.cnfol.com",),
              "cnfol2": ("sc.stock.cnfol.com",),
              "cnfol3": ("stock.cnfol.com",),
              "cnstock1": ("news.cnstock.com",),
              "cs1": ("cs.com.cn",), "cs2": ("www.cs.com.cn",),
              "eastmoney1": ("guba.eastmoney.com", "stock.eastmoney.com", "finance.eastmoney.com",),
              "hexun1": ("stock.hexun.com",),
              "ifeng1": ("finance.ifeng.com", "news.ifeng.com", "tech.ifeng.com"),
              "ifeng2": ("app.finance.ifeng.com",),
              "jfinfo1": ("m.jfinfo.com", "stock.jfinfo.com"), "jfinfo2": ("www.jfinfo.com",),
              "jrj1": ("stock.jrj.com.cn", "finance.jrj.com.cn", "usstock.jrj.com.cn"),
              "jrj2": ("http://finance.jrj.com.cn", ),
              "laoqianzhuang1": ("laoqianzhuang.com", "538538.com"),
              "p5w1": ("www.p5w.net",),
              "qq1": ("finance.qq.com", "tech.qq.com",),
              "stcn1": ("stcn.com",),
              "stockstar1": ("stock.stockstar.com",),
              "tjqka1": ("news.10jqka.com.cn", "field.10jqka.com.cn", "stock.10jqka.com.cn"),
              "wangyi1": ("money.163.com", "auto.163.com", "tech.163.com",),
              "xinhua081": ("stock.xinhua08.com", "world.xinhua08.com", "forex.xinhua08.com"),
              "xinhua2": ("www.xinhuanet.com", ),
              "yicai1": ("www.yicai.com",),
              "wallstreetcn1": ("wallstreetcn.com",),
              "sina1": ("finance.sina.com.cn",),
              "sina2": ("sh.house.sina.com.cn",),
              "sina3": ("auto.sina.com.cn",),
              "sina4": ("tech.sina.com.cn",),
              "sina5": ("mil.news.sina.com.cn",),
              "xinhuanet1": ("news.xinhuanet.com",),
              "sohu1": ("stock.sohu.com",),
              "sohu2": ("auto.sohu.com", "it.sohu.com"),
              "sohu3": ("business.sohu.com",),
              "hongzhoukan1": ("news.hongzhoukan.com",),
              "cnr1": ("cnr.cn", "china.cnr.cn", "news.cnr.cn", "finance.cnr.cn", "www.cnr.cn"),
              "tojingji1": ("www.21jingji.com",),
              "people1": ("military.people.com.cn", "tc.people.com.cn", "finance.people.com.cn",
                          "scitech.people.com.cn", "it.people.com.cn", "politics.people.com.cn"),
              "nbd1": ("www.nbd.com.cn",),
              "ce1": ("finance.ce.cn",),
              "chinanews1": ("finance.chinanews.com",),
              "huanqiu1": ("world.huanqiu.com",),
              "cngold1": ("www.cngold.org",),
              "caixin1": ("caixin.com", "finance.caixin.com", "www.caixin.com", "companies.caixin.com", ),
              "xcf1": ("www.xcf.cn",),
              "xuangubao1": ("xuangubao.cn",),
              "mscbsc1": ("www.mscbsc.com", ),
              "p581881": ("www.58188.com", ),
              "bjx1": ("huanbao.bjx.com", ),
              "techweb1": ("www.techweb.com",),
              "ebrun1": ("www.ebrun.com",),
              "lmjx1": ("www.lmjx.com", ),
              "p1631": ("tech.163.com", ),
              "ometal1": ("www.ometal.com", ),
              "hc3601": ("info.chem.hc360.com",),
              "donews1": ("www.donews.com",),
              "bmlink1": ("www.bmlink.com", ),
              "china5e1": ("www.china5e.com",),
              "p21food1": ("news.21food.cn", ),
              "iresearch1": ("news.iresearch.cn",),
              "cheaa1": ("news.cheaa.com",),
              "stnn1": ("news.stnn.cc",),
              "carnoc1": ("news.carnoc.com",),
              "tnc1": ("www.tnc.com.cn",),
              "texnet1": ("info.texnet.com.cn",),
              "chinaventure1": ("www.chinaventure.com.cn",),
              "chinabreed1": ("www.chinabreed.com",),
              "techfood1": ("www.techfood.com",),
              "laohucaijing1": ("www.laohucaijing.com",),
              "machine3651": ("news.machine365.com/",),
              "chem171": ("www.chem17.com",),
              "cpnn1": ("www.cpnn.com.cn",),
              "ybzhan1": ("www.ybzhan.cn",),
              "d1ev1": ("www.d1ev.com",),
              "tpy8881": ("www.tpy88.cn",),
              "takungpao1": ("finance.takungpao.com",),
              "eepw1": ("www.eepw.com.cn",),
              "aweb1": ("news.aweb.com.cn",),
              "p21jingji1": ("www.21jingji.com",),
              "cctv1": ("jingji.cctv.com",),
              "cri1": ("news.cri.cn",),
              "ftchinese1": ("www.ftchinese.com",),
              "ccd1": ("news.ccd.com.cn",),
              "smm1": ("news.smm.cn",),
              "gongkong1": ("www.gongkong.com",),
              "zgny1": ("www.zgny.com",),
              "tom1": ("finance.tom.com",),
              "banyuetan1": ("www.banyuetan.org",),
              "lswb1": ("www.lswb.com",),
              "bbtnews1": ("www.bbtnews.com.cn",),
              "btime1": ("item.btime.com",),
              "cdsb1": ("static.cdsb.com",),
              "cyzone1": ("www.cyzone.cn",),
              "dahe1": ("news.dahe.cn",),
              "dayoo1": ("news.dayoo.com",),
              "chinabreed1": ("www.chinabreed.com",),
              }


def content_parse(func, raw_html, item):
    """ 内容解析统一入口 """
    if func in _func_host:
        root = HTML(raw_html.text)
        globals()[func](root, item)
    else:
        content = []
        for block in Article(raw_html).main_text:
            content.append(''.join([line[0] for line in block if line]))
        item.set('content', '\n'.join(content))


def aastocks1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//span[contains(@id,'spanContent')]//text()[position()<=last()-3]")))


def cailianpress1(root, item):
    """  """
    #item.set('content', "".join(root.xpath("//div[@id='entries']//li[@class='content']//*[not(@class='state')]//text()")))
    item.set('content', "".join(root.xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/text()')))


def ccstock1(root, item):
    """  """
    item.set('content', "".join(root.xpath("//div[@class='content']/p/text()")))


def cfi1(root, item):
    """  """
    content = "".join(root.xpath(".//div[contains(@id,'tdcontent')]//text()"))
    content = re.sub(r"\[.*?\]", "", content)
    item.set('content', re.sub(ur">>下一页", "", content))


def cfi2(root, item):
    """stock.cfi.cn"""
    content = "".join(root.xpath(".//div[contains(@id,'tdcontent')]//text()"))
    item.set('content', content)


def china1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'tdcontent')]//text()")))


def china2(root, item):
    content = "".join(root.xpath("//div[@id='fontzoom']/p/text()"))
    item.set('content', content)


def cnfol1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'Content')]//text()")))


def cnfol2(root, item):
    """  """
    # print root.xpath(".//div[contains(@div,'Article')]/text()")
    item.set('content', "".join(root.xpath(".//div[contains(@div,'Article')]//text()")))


def cnfol3(root, item):
    """http://stock.cnfol.com/"""
    item.set('content', "".join(root.xpath(".//div[contains(@class,'Article')]//text()")))


# http://news.cnstock.com/industry/sid_rdjj/
def cnstock1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'qmt_content_div')]//text()")))


# http://www.cs.com.cn/sylm/cstop10/
# http://www.cs.com.cn/ssgs/hyzx/
def cs1(root, item):
    """"""
    item.set('content', "".join(root.xpath(".//div[contains(@class,'Dtext')]//p//text()")))


def cs2(root, item):
    content = "".join(root.xpath("//div[@class='article-t hidden']/p/text()"))
    item.set("content", content)


# http://stock.eastmoney.com/news/cbkjj.html
def eastmoney1(root, item):
    """  """
    content = "".join(root.xpath(".//div[@class='newsContent']/div[@id='ContentBody']//p//text()"))
    logging.debug(content)
    item.set('content', content)


def hexun1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'artibody')]//p//text()")))


def ifeng1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[@id='main_content']//p//text()")))


def jfinfo1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@class,'mainCont contMain')]//p//text()")))


def jrj1(root, item):
    """  """
    item.set('content', "".join(root.xpath("//div[@class='titmain']/div[@class='texttit_m1']/p[not(@class='linknew')]//text()")))


def laoqianzhuang1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'atc-content')]//text()")))


def p5w1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@class,'zwleft')]//div[@class='text']//p//text()")))


def qq1(root, item):
    """  """
    time_text = "".join(root.xpath("//div[@class='a_Info']/span[@class='a_time']/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    item.set('content', "".join(root.xpath(".//div[contains(@id,'Cnt-Main-Article-QQ')]/p[not(contains(@style,'COLOR: red'))]//text()")))


def stcn1(root, item):
    """  """
    item.set('content', "".join(root.xpath("//div[@id='ctrlfscont']//text()")))


# http://stock.stockstar.com/list/sectors.htm
def stockstar1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'container-article')]/p//text()")))


def tjqka1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[@class='atc-content']/p//text()")))


def wangyi1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'endText')]/p[not(@class='otitle')]//text()")))


def xinhua081(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@id,'ctrlfscont')]//text()")))


def yicai1(root, item):
    """  """
    item.set('content', "".join(root.xpath(".//div[contains(@class,'m-text')]//text()")))


def wallstreetcn1(root, item):
    """  """
    item.set('title', "".join(root.xpath("//div[@class='page-article-title']/div[@class='title-text']/text()")).strip())
    item.set('content', "".join(root.xpath("//div[@class='page-article-content']/p//text()")))


def sina1(root, item):
    """  """
    content = "".join(root.xpath("//div[@id='artibody']/*[not(@class='xb_new_finance_app')][name()!='script']//text()"))
    item.set('content', content)


def sina2(root, item):
    """  """
    item.set('content', "".join(root.xpath("//div[@id='artibody']/p//text()")))


def sina4(root, item):
    content = "".join(root.xpath("//div[@id='artibody']/p/text()"))
    item.set("content", content)


def sina5(root, item):
    content = "".join(root.xpath("//div[@id='article']/p/text()"))
    item.set("content", content)


def xuangubao1(root, item):
    """  """
    item.set('content', "".join(root.xpath("//div[@class='article']//p[@class!='article-content-download']//text()")))


def jrj2(root, item):
    time_text = "".join(root.xpath("//div[@class='titmain']/p[@class='inftop']/span[1]/text()"))
    time_text = time_text.strip()
    item.set('timestamp', my_utils.get_timestamp(time_text))
    item.set('content', "".join(root.xpath("//div[@class='titmain']/div[@class='texttit_m1']/p/text()")))


def huanqiu1(root, item):
    content = "".join(root.xpath("//div[@class='la_con']/p/text()"))
    item.set('content', content)


def mscbsc1(root, item):
    content = "".join(root.xpath("//div[@id='articlebody']/p/text()"))
    item.set('content', content)


def p581881(root, item):
    content1 = "".join(root.xpath("//div[@id='article']//p/text()"))
    item.set('content', content1)


def xinhua2(root, item):
    time_text = "".join("//div[@class='source']/span[@class='time']")
    time_text = time_text.strip()
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='p-detail']/p/text()"))
    item.set('content', content)


def bjx1(root, item):
    time_text = "".join(root.xpath("//div[@class='list_copy']/b/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='content']/p/text()"))
    item.set('content', content)
_func_host

def chinanews1(root, item):
    content = "".join(root.xpath("//div[@class='left_zw']/p/text()"))
    item.set('content', content)


def techweb1(root, item):
    time_text = "".join(root.xpath("//div[@class='infos']/span[1]/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='content']/p/text()"))
    item.set('content', content)


def ebrun1(root, item):
    content = "".join(root.xpath("//div[@class='post-text']/p/text()"))
    item.set('content', content)


def caixin1(root, item):
    content = "".join(root.xpath("//div[@id='Main_Content_Val']/p/text()"))
    item.set('content', content)


def cnr1(root, item):
    content = "".join(root.xpath("//div[@class='TRS_Editor']/p/text()"))
    item.set('content', content)


def nbd1(root, item):
    abstract = "".join(root.xpath("//div[@class='g-article-abstract']/p/text()"))
    content = "".join(root.xpath("//div[@class='g-articl-text']/p/text()"))
    item.set('abstract', abstract)
    item.set('content', content)


def lmjx1(root, item):
    content = "".join(root.xpath("//div[@id='i_art_main']/content/p/text()"))
    item.set('content', content)


def ce1(root, item):
    content = "".join(root.xpath("//div[@class='TRS_Editor']/p/text()"))
    item.set('content', content)


def p1631(root, item):
    content = "".join(root.xpath("//div[@id='endText']/p/text()"))
    item.set('content', content)


def ometal1(root, item):
    content = "".join(root.xpath("//div[@id='fontzoom']//text()"))
    # print "content", content
    item.set('content', content)


def hc3601(root, item):
    time_text = "".join(root.xpath("//span[@id='endData']/text()"))
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@id='artical']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def donews1(root, item):
    time_text = "".join(root.xpath("//p[@class='fl']/span[2]/text()"))
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='article-con']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def people1(root, item):
    time_text = "".join(root.xpath("//div[@class='box01']/div[@class='fl']/text()"))
    time_text = "".join(time_text.split()[:1])
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@id='rwb_zw']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def bmlink1(root, item):
    content = "".join(root.xpath("//div[@class='newsinfo_cont']/p/text()"))
    item.set('content', content)


def china5e1(root, item):
    time_text = "".join(root.xpath("//div[@class='showtitle']/div[@class='showtitinfo']/text()"))
    time_text = time_text.split()[0]
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@id='showcontent']/div[1]/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def p21food1(root, item):
    time_text = "".join(root.xpath("//div[@class='news_detail_t']/div[@class='ws_det_p2']/i[1]/text()"))
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='news_detail_t']/div[@class='ws_det_p3']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def iresearch1(root, item):
    time_text = "".join(root.xpath("//div[@class='origin']/em/text()"))
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='m-article']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def cheaa1(root, item):
    time_text = "".join(root.xpath("//div[@id='NewsInfo']/text()"))
    time_text = "".join(time_text.strip().split()[:2])
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@id='ctrlfscont']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def stnn1(root, item):
    content = "".join(root.xpath("//div[@class='article-content fontSizeSmall BSHARE_POP']/p/text()"))
    item.set('content', content)


def carnoc1(root, item):
    time_text = "".join(root.xpath("//span[@id='pubtime_baidu']/text()"))
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@id='newstext']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def jfinfo2(root, item):
    time_text = "".join(root.xpath("//div[@class='t-tit']/span[1]/text()"))
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='t-context f16 picture']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def tnc1(root, item):
    time_text = "".join(root.xpath("//div[@class='article-title']/p/text()"))
    time_text = " ".join(time_text.split()[:2])
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='article-content c-mb-20']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def texnet1(root, item):
    time_text = "".join(root.xpath("//p[@class='line22 fontgrey']/text()"))
    time_text = " ".join(time_text.split()[1:3])
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='detail-text line25 font14px']/div/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def chinaventure1(root, item):
    time_text = "".join(root.xpath("//div[@class='details_01_l']/span[3]/text()"))
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='content_01 m_t_30 detasbmo']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def techfood1(root, item):
    content = "".join(root.xpath("//div[@id='zoom']/p/text()"))
    item.set('content', content)


def laohucaijing1(root, item):
    content = "".join(root.xpath("//div[@id='test']/p/text()"))
    item.set('content', content)


def machine3651(root, item):
    time_text = "".join(root.xpath("//div[@class='newliIn_Sti']/text()"))
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@class='newliIn_Zti']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def chem171(root, item):
    time_text = "".join(root.xpath("//div[@class='newsTime']/dl/dt/text()")[0])
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='newsContent']/div/text()"))
    item.set('content', content)


def cpnn1(root, item):
    content = "".join(root.xpath("//div[@class='cpnn-con-zhenwen']/p/text()"))
    item.set('content', content)


def ybzhan1(root, item):
    time_text = "".join(root.xpath("//span[@class='time']/text()")[0])
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='newsContent']/div/text()"))
    item.set('content', content)


def d1ev1(root, item):
    content = "".join(root.xpath("//div[@id='showall233']/p/text()"))
    item.set('content', content)


def tpy8881(root, item):
    content = "".join(root.xpath("//div[@id='article']/div/span/span/text()"))
    item.set('content', content)


def takungpao1(root, item):
    time_text = "".join(root.xpath("//div[@class='tkp_con_author']/span[1]/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='tkp_content']//text()"))
    item.set('content', content)


def eepw1(root, item):
    content = "".join(root.xpath("//span[@id='contentlabels']/p/text()"))
    item.set('content', content)


def aweb1(root, item):
    time_text = "".join(root.xpath("//div[@class='newsLeft newscontentB']/h5/text()")[0])
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='conT f14px'][1]/p/text()"))
    item.set('content', content)


def p21jingji1(root, item):
    date_text = "".join(root.xpath("//p[@class='Wh']/span[1]/text()"))
    time_text = "".join(root.xpath("//span[@class='hour']/text()"))
    time_text = date_text + " " + time_text
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='detailCont']/p/text()"))
    item.set('content', content)


def cctv1(root, item):
    content = "".join(root.xpath("//div[@class='cnt_bd']/p/text()"))
    item.set('content', content)


def cri1(root, item):
    time_text = "".join(root.xpath("//span[@id='acreatedtime']/text()"))
    # print time_text
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='abody']/p/text()"))
    item.set('content', content)


def ftchinese1(root, item):
    # print "root", root
    if root is None:
        # print "warning: root is None"
        return
    time_text = "".join(root.xpath("//span[@class='story-time']/text()"))
    ts = my_utils.get_timestamp(time_text)
    content = "".join(root.xpath("//div[@id='story-body-container']/p/text()"))
    item.set('timestamp', ts)
    item.set('content', content)


def ccd1(root, item):
    content = "".join(root.xpath("//div[@class='detail-box']/p/text()"))
    item.set('content', content)


def smm1(root, item):
    time_text = "".join(root.xpath("//p[@class='news-tips']/label[1]/span/text()"))
    time_text = "".join(time_text.split()[:2])
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='news-main']/p/text()"))
    item.set('content', content)


def gongkong1(root, item):
    time_text = "".join(root.xpath("//span[@class='f1405'][3]/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='article']/p/text()"))
    item.set('content', content)


def zgny1(root, item):
    time_text = "".join(root.xpath("//p[@class='xinXi']/text()"))
    time_text = "".join(time_text.split()[3:5])
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='wenZi_02']/p/text()"))
    item.set('content', content)


def sohu3(root, item):
    time_text = "".join(root.xpath("//span[@id='news-time']/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//article[@id='mp-editor']/p/text()"))
    item.set('content', content)


def tom1(root, item):
    time_text = "".join(root.xpath("//span[@class='infor_time']/text()"))
    time_text = time_text.strip()
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='news_box_text']/p/text()"))
    item.set('content', content)


def banyuetan1(root, item):
    time_text = "".join(root.xpath("//div[@class='detail_tit_time']/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='detail_content']/p/text()"))
    item.set('content', content)


def lswb1(root, item):
    time_text = "".join(root.xpath("//ol[@class='breadcrumb']/li[1]/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='article-content']/p/text()"))
    item.set('content', content)


def bbtnews1(root, item):
    time_text = "".join(root.xpath("//div[@class='info']/span/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='pageContent']/p/text()"))
    item.set('content', content)


def btime1(root, item):
    time_text = "".join(root.xpath("//span[@class='col time']/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='content-pure']/p/text()"))
    item.set('content', content)


def cdsb1(root, item):
    content = "".join(root.xpath("//article[@class='cd-article_content']/p/text()"))
    item.set('content', content)


def cyzone1(root, item):
    content = "".join(root.xpath("//article[@class='cd-article_content']/p/text()"))
    item.set('content', content)


def dahe1(root, item):
    content = "".join(root.xpath("//div[@id='mainCon']/p/text()"))
    item.set('content', content)


def dayoo1(root, item):
    time_text = "".join(root.xpath("//span[@class='time']/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@id='text_content']/p/text()"))
    item.set('content', content)


def chinabreed1(root, item):
    time_text = "".join(root.xpath("//div[@class='artInfo']/span[@id='pub_date']/text()"))
    ts = my_utils.get_timestamp(time_text)
    item.set('timestamp', ts)
    content = "".join(root.xpath("//div[@class='blkContainerSblk']/div[@id='artibody']/div/text()"))
    item.set('content', content)
