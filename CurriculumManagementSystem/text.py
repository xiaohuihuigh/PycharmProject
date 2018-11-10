# #coding:utf-8
# '''
# n为当天晚上要查看的洞
# list1为肯能是兔子藏身的洞的集合
# set2为当查看n后，没有抓到兔子，兔子可能藏身的集合
# '''
# def getNewSet(n,list1):
#     set2 = set()
#     for i in list1:
#         if i+1 != n and i+1<=5:
#             set2.add(i+1)
#         if i-1 != n and i-1>=1:
#             set2.add(i-1)
#     return  set2
#
# import Queue
# if __name__== '__main__':
#     '''
#     bfs进行搜索，首先将初始情况加入队列，
#     1.当队列部不空时：
#         2.如果已经得到了结果，那就结束，跳转到（7.）
#         3.取出队列的第一个值
#         4.分别检查5个洞，
#             5.如果检查之后兔子的藏身洞变少，那就将这个洞加入到队列中;
#             6.如果检查后兔子没有藏身之处，则已经找到结果
#               将结果赋值给ans同时设置已找到结果标志，并跳出循环
#     7.输出最后记录的结果
#     8.根据得到的结果，找出每一步后兔子藏身之处
#     '''
#     Q = Queue.Queue()
#     # for i in range(1,6):
#     Q.put((0,set([1,2,3,4,5]),[]))
#     rn = 0
#     ans = []
#     # 1.
#     while not Q.empty() :
#         # 2.
#         if rn == 1:
#             break
#         # 3.
#         n,set1,list1 = Q.get()
#         # 4.
#         for i in range(1,6):
#             tlist = list1[:]
#             set2 = getNewSet(i,set1)
#             # 5.
#             if len(set1)>=len(set2):
#
#                 tlist.append(n)
#                 # print set1,i, set2,tlist
#                 Q.put((i,set2,tlist))
#             # 6.
#             if not set2:
#                 tlist.append(i)
#                 ans = tlist
#                 rn = 1
#                 break
#     # 7.
#     print ans
#     # 8.
#     set3 = set([1,2,3,4,5])
#     for i in ans[1:]:
#         set3 = getNewSet(i,set3)
#         print i,set3


def log(n,a):
    ans = 0
    while n / a:
        ans += 1
        n /= a
    return ans

def getTime(n,i):
    ans = 0
    t = log((n - 1),i)
    ans = (i-1)*t+(n-1)/(i**t)
    return ans
e = 10**50
s = 1
mid = (s+e)/2
# while s<e:
#     # print s,e
#     print getTime(mid,3) , getTime(mid,2)
#     if getTime(mid,3) - getTime(mid,2) == 1:
#         print mid
#         break
#     if getTime(mid,3) - getTime(mid,2) > 1:
#         s = mid+1
#     else:
#         e = mid
#     mid = (s+e)/2
# for i in range(1,83):
#     print i,getTime(i,3)

# for i in range(1,1000):
#     print i,getTime(i,2)
# for i in range(1,1000000000,1000000):
#     t = 10**i
#     print i
#     if getTime(t,3)<getTime(t,2):
#         print i,getTime(t,3)
#         break

# dp[n] = i-1 + dp [(n-1)/i+1]
dp = [0] *1000
dp[1] = 0
dp[2] = 1
dp[3] = 2
for i in range(4,1000):
    dp[i] = 2 + dp[(i-1)/3+1]
for i in range(1,1000):
    print dp[i],getTime(i,3)


























