from BeautifulSoup import BeautifulSoup

import re
with open('homepage.html','r')as f:
    avb = f.read()

soup = BeautifulSoup(avb)
# print str(soup)
TermInfo = soup.find(name='font',color='red').string.strip()
print TermInfo
StudentInfo= [x.string.strip() for x in soup.findAll(name='div',style="line-height: 23px;")]
print StudentInfo
