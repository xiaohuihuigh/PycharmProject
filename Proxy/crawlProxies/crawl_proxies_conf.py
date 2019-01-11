# coding:utf-8
import os
import platform
if platform.python_version()[0] == '3':
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser
def set_config():
    fp = 'crawlProxies/crawlProxies.conf'
    conf = ConfigParser()
    conf.read(os.path.join( os.getcwd(), fp))
    iliststr = conf.get('all','name')
    iliststr = iliststr.strip('[]').split(', ')
    ilist = [i.strip("'") for i in iliststr]
    for i in ilist:
        if not conf.has_section(i):
            conf.add_section(i)
            if i == 'mimvp':
                conf.set(i,'yn','True')
            else:
                conf.set(i, 'yn', 'False')
            conf.set(i,'last_time','0')
            conf.set(i,'interval_time','60')
        with open(fp,'w')as f:
            conf.write(f)