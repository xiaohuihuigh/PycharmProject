#coding:utf-8
from BeautifulSoup import BeautifulSoup
import re
import numpy
with open('deletecoursetable.html','r')as f:
    avb = f.read()

soup = BeautifulSoup(avb)
# print str(soup)
table = soup.findAll(name='table',attrs={"class":"tbllist"})[0]

table.col = len(table.findAll(name = 'th'))
table.title = [x.string.strip()  for x in  table.findAll('th')]

tablec = [x.string.strip() if x.string!=None else  x.string  for x in table.findAll(name='td')]
courseinfo = numpy.array(tablec[1:]).reshape((-1,table.col))
print  courseinfo
for j in range(len(table.title)):
    print table.title[j],
print ''
for i in range(len(courseinfo)):
    for j in range(len(table.title)):
        # if i == 0:
        #     print talbe1.ttitle[j],
        print courseinfo[i][j],
    print ''
