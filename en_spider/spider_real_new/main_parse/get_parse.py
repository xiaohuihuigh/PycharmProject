#! /usr/bin/python
# -*- encoding:utf-8 -*-
# 需要在这里手工导入类

import logging
import sys
import os
from base_parse import BaseParse

#from aastocks_parse import Aastocks1

from cailianpress_parse import Cailianpress1
'''
from cnstock_parse import Cnstock1, Cnstock2, Cnstock3
from eastmoney_parse import Eastmoney1, Eastmoney2, Eastmoney3
from stcn_parse import Stcn1, Stcn2
from stockstar_parse import Stockstar1
from tjqka_parse import Tjqka1, Tjqka2, Tjqka3, Tjqka4
from wallstreetcn_parse import Wallstreetcn1
from ccstock_parse import Ccstock1
from cs_parse import Cs1, Cs2
from jrj_parse import Jrj1, Jrj3
from laoqianzhuang_parse import Laoqianzhuang1
from sina_parse import Sina1, Sina2, Sina3, Sina4
from yicai_parse import Yicai1
from qq_parse import Qq1, Qq2
from ifeng_parse import Ifeng1
from stockstar_parse import Stockstar1
from wangyi_parse import Wangyi1, Wangyi2
from p5w_parse import P5w1
from xinhua08_parse import Xinhua081
from jfinfo_parse import Jfinfo1
from hexun_parse import Hexun1, Hexun2
from cnfol_parse import Cnfol1, Cnfol2, Cnfol3
from cfi_parse import Cfi1, Cfi2
from microbell_parse import Microbell1
from china_parse import China1
from xuangubao_parse import Xuangubao1, Xuangubao2
from z50_jrj_parse import Jrj2
from z54_huanqiu_parse import Huanqiu1
from z56_mscbsc_parse import Mscbsc1
from z58_p58188_parse import P581881
from xinhua08_parse import Xinhua2
from z61_bjx_parse import Bjx1
from z73_chinanews_parse import Chinanews1
from z83_techweb_parse import Techweb1, Techweb2
from z85_ebrun_parse import Ebrun1
from z107_caixin_parse import Caixin1
from z108_cnr_parse import Cnr1
from z109_nbd_parse import Nbd1
from z110_lmjx_parse import Lmjx1
from z111_ce_parse import Ce1
from z114_p163_parse import P1631, P1632, P1633
from z117_ometal_parse import Ometal1
from z118_hc360_parse import Hc3601
from z119_donews_parse import Donews1
from z120_people_parse import People1, People2, People3, People4, People5
from z126_bmlink_parse import Bmlink1
from z132_china5e_parse import China5e1
from z138_p21food_parse import P21food1
from z139_iresearch_parse import Iresearch1, Iresearch2
from z140_cheaa_parse import Cheaa1
from z146_stnn_parse import Stnn1
from z147_carnoc_parse import Carnoc1
from z148_jfinfo_parse import Jfinfo2
from z149_tnc_parse import Tnc1
from z150_texnet_parse import Txtnet1
from z151_chinaventure_parse import Chinaventure1
from z152_chinabreed_parse import Chinabreed1
from z153_techfood_parse import Techfood1
from z155_laohucaijing_parse import Laohucaijing1
from z156_machine365_parse import Machine3651
from z157_chem17_parse import Chem171
from z158_cpnn_parse import Cpnn1
from z159_ybzhan_parse import Ybzhan1
from z160_d1ev_parse import D1ev1, D1ev2
from z161_tpy888_parse import Tpy8881
from z162_takungpao_parse import Takungpao1
from z163_eepw_parse import Eepw1
from z164_aweb_parse import Aweb1
from z165_p21jingji_parse import P21jingji1
from z168_p36kr_parse import P36kr1
from z170_cctv_parse import Cctv1
from z171_cri_parse import Cri1
from z174_ftchinese_parse import Ftchinese1
from z180_ccd_parse import Ccd1
from z181_smm_parse import Smm1
from z185_gongkong_parse import Gongkong1
from z186_zgny_parse import Zgny1
from z188_sohu_parse import Sohu1
from z191_tom_parse import Tom1
from z194_banyuetan_parse import Banyuetan1
from z197_lswb_parse import Lswb1
from z202_bbtnews_parse import Bbtnews1
from z205_btime_parse import Btime1
from z207_cdsb_parse import Cdsb1
from z208_cyzone_parse import Cyzone1
from z216_dahe_parse import Dahe1
from z220_dayoo_parse import Dayoo1
'''
logger = logging.getLogger("parse")


class Parse(object):
    """ class: [sid-0,sid-1...] """
    _TITLE_CLASS = {
        "Cnstock1": [8, 22], "Cnstock2": [10, 63], "Cnstock3": [40],
        "Tjqka1": [13], "Tjqka2": [15, 20, 33], "Tjqka3": [41], "Tjqka4": [51, 86, 87, 88],
        "Laoqianzhuang1": [19],
        "Hexun2": [25], "Hexun1": [],
        "Jrj1": [1], "Jrj2": [50, 105, 106], "Jrj3": [57, 101, 102, 103, 104],
        "Jfinfo1": [31],
        "Xinhua081": [30], "Xinhua2": [59],
        "Yicai1": [21],
        "Stcn1": [5, 34], "Stcn2": [26],
        "Ifeng1": [24],
        "Stockstar1": [16],
        "Wangyi1": [27], "Wangyi2": [28],
        "Sina1": [12], "Sina2": [68, 69, 70], "Sina3": [71], "Sina4": [72],
        "Aastocks1": [14],
        "Ccstock1": [9, 142, 143, 144, 145],
        "Cs1": [7, 18], "Cs2": [84, 128, 129, 130, 131, 182, 183, 184],
        "Cailianpress1": [6], "Cailianpress2": [3], "Cailianpress3": [2], "Cailianpress4": [39],
        "Eastmoney1": [11], "Eastmoney2": [17], "Eastmoney3": [60, 64, 77, 78, 79, 80, 81, 82],
        "P5w1": [29],
        "Qq1": [23], "Qq2": [154],
        "Wallstreetcn1": [4, 141],
        "Cnfol1": [32], "Cnfol2": [52], "Cnfol3": [55, 62, 65, 66, 67],
        "Cfi1": [35, 96, 97, 98, 99, 100], "Cfi2": [53, 89, 90, 91, 92, 93, 94, 95],
        "Microbell1": [36],
        "China1": [37, 112, 113],
        "Xuangubao1": [38], "Xuangubao2": [42],
        "Huanqiu1": [54],
        "Mscbsc1": [56, 76],
        "P581881": [58],
        "Bjx1": [61, 198, 199, 200, 201],
        "Chinanews1": [73, 74, 75],
        "Techweb1": [83], "Techweb2": [178, 179],
        "Ebrun1": [85],
        "Caixin1": [107],
        "Cnr1": [108],
        "Nbd1": [109],
        "Lmjx1": [110],
        "Ce1": [111],
        "P1631": [114], "P1632": [115], "P1633": [116],
        "Ometal1": [117],
        "Hc3601": [118],
        "Donews1": [119, 173],
        "People1": [120], "People2": [121, 125], "People3": [122], "People4": [123], "People5": [124],
        "Bmlink1": [126, 127],
        "China5e1": [132, 133, 134, 135, 136, 137],
        "P21food1": [138],
        "Iresearch1": [139], "Iresearch2": [193],
        "Cheaa1": [140],
        "Stnn1": [146],
        "Carnoc1": [147],
        "Jfinfo2": [148],
        "Tnc1": [149],
        "Txtnet1": [150],
        "Chinaventure1": [151],
        "Chinabreed1": [152],
        "Techfood1": [153],
        "Laohucaijing1": [155],
        "Machine3651": [156],
        "Chem171": [157, 187],
        "Cpnn1": [158],
        "Ybzhan1": [159],
        "D1ev1": [160], "D1ev2": [190],
        "Tpy8881": [161],
        "Takungpao1": [162, 209, 210, 211, 212, 213, 214, 215],
        "Eepw1": [163],
        "Aweb1": [164],
        "P21jingji1": [165, 166, 167],
        "P36kr1": [168],
        "Cctv1": [170],
        "Cri1": [171, 172],
        "Ftchinese1": [174, 175, 176, 177],
        "Ccd1": [180],
        "Smm1": [181],
        "Gongkong1": [185],
        "Zgny1": [186],
        "Sohu1": [188, 189],
        "Tom1": [191, 192],
        "Banyuetan1": [194, 195, 196],
        "Lswb1": [197],
        "Bbtnews1": [202, 203, 204],
        "Btime1": [205, 206],
        "Cdsb1": [207],
        "Cyzone1": [208],
        "Dahe1": [216, 217, 218, 219],
        "Dayoo1": [220, 221, 222, 223, 224, 225]
    }

    def __init__(self):
        """ set self._DICT_SITE sid: [title-class, content-class] """
        self._DICT_SITE = {}
        for css in self._TITLE_CLASS:
            for sid in self._TITLE_CLASS[css]:
                self._DICT_SITE[sid] = css
        self._TITLE_CLASS = {}

    def get_class(self, sid):
        """ get parse class """
        if sid not in self._TITLE_CLASS:
            if sid in self._DICT_SITE:
                self._TITLE_CLASS[sid] = globals()[self._DICT_SITE[sid]]()
            else:
                self._TITLE_CLASS[sid] = BaseParse()
                logger.error("sid %s not have class. " % sid)
        return self._TITLE_CLASS[sid]
