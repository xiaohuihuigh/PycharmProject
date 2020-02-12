# coding:utf-8
import os
import platform
from Code import etc
if platform.python_version()[0] == '3':
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

#设置
def set_config(conf):
    iliststr = conf.get('all','name')
    iliststr = iliststr.strip('[]').split(', ')
    ilist = [i.strip("'") for i in iliststr]

    for i in ilist:
        conf_sub = ConfigParser()
        sub_conf = os.path.join(etc.conf_path,i+'.conf')
        conf_sub.read(sub_conf)

        if not conf_sub.has_section(i):
            conf_sub.add_section(i)
            if i == 'mimvp':
                conf_sub.set(i,'yn','True')
            else:
                conf_sub.set(i, 'yn', 'False')
            conf_sub.set(i,'last_time','0')
            conf_sub.set(i,'interval_time','60')

        with open(sub_conf,'w')as f:
            conf_sub.write(f)
