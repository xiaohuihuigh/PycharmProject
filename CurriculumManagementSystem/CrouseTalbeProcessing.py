#coding:utf-8
from BeautifulSoup import BeautifulSoup
import re
import numpy
with open('coursetable.html','r')as f:
    avb = f.read()

soup = BeautifulSoup(avb)
# print str(soup)
table1,table2 = soup.findAll(name='table',attrs={"class":"tbllist"})
StudentcInfo = [x.string.strip() if x.string!= None else x.string for x in table1.findAll(name = 'div')]

table1.col = len(table1.findAll(name = 'th'))
table1.title = [x.string.strip()  for x in  table1.findAll(name='th')]

table1c = [x.string.strip() if x.string!=None else  x.string  for x in table1.findAll(name='td')]
courseinfo = numpy.array(table1c[2:-1]).reshape((-1,table1.col))

# for j in range(len(table1.title)):
#     print talbe1.title[j],
# print ''
# for i in range(len(courseinfo)):
#     for j in range(len(talbe1.ttitle)):
#         # if i == 0:
#         #     print talbe1.ttitle[j],
#         print courseinfo[i][j],
#     print ''
'''
序号 课程号 课程名 教师号 教师名 学分 上课时间 上课地点 校区 答疑时间 答疑地点 
A 00864102 计算机技术基础A(1)(理工类) 1012 王文 2 四3-4 含上机 DJ303 本部 三7-8 D319 
A 00864102 计算机技术基础A(1)(理工类) 1012 王文 2 四3-4 含上机 DJ303 本部 三7-8 D319 
A 00864102 计算机技术基础A(1)(理工类) 1012 王文 2 四3-4 含上机 DJ303 本部 三7-8 D319 
'''
# print table1.row,table1.col
# print table1.row
# for i in StudentcInfo:
#     print i
table2.col = len(table2.findAll(name = 'th'))
print table2.row,table2.col



table2.title = [x.string.strip() if x.string != None else x.string for x in  table2.findAll(name='th')]
#
table2c = [x.string.strip() if x.string!=None else  x.string  for x in table2.findAll(name='td')]
print len(table2c)
timetableinfo = numpy.array(table2c).reshape((-1,table2.col))
print len(table2.title)
print table2.title[1]
for j in range(len(table2.title)):
    print table2.title[j],
print ''
for i in range(len(timetableinfo)):
    for j in range(table2.col):
        # if i == 0:
        #     print title[j],
        print timetableinfo[i][j],
    print ''
'''
序号 课程号 课程名 教师号 教师名 学分 上课时间 上课地点 校区 答疑时间 答疑地点 
A 00864102 计算机技术基础A(1)(理工类) 1012 王文 2 四3-4 含上机 DJ303 本部 三7-8 D319 
A 00864102 计算机技术基础A(1)(理工类) 1012 王文 2 四3-4 含上机 DJ303 本部 三7-8 D319 
A 00864102 计算机技术基础A(1)(理工类) 1012 王文 2 四3-4 含上机 DJ303 本部 三7-8 D319 
'''