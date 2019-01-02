import re
import json
with open('test.html','r')as f:
    sp = f.read()
url = re.findall(r'<link rel="amphtml" href="(.*)">',sp)
print url
# <link rel="amphtml" href="https://xw.qq.com/amphtml/20181228007102/STO2018122800710200">