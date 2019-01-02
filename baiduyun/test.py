# import subprocess
# # import os
# with open('a.txt','a')as f:
#     t = subprocess.Popen('curl -X POST -k -L www.baidu.com   '
#                          '',stdout=f)
#     # t = subprocess.Popen('ls', stdout=f)
# # tl = t.split('\n')
# # print tl
# # print t
a = 2.25
s = "%.2fG%.1fG"%(a,a)
u = 1.00
t = "Your Storage Status: %.2fG/%.2fG (%.2f%%)"%(u,a,u/a*100)
print t