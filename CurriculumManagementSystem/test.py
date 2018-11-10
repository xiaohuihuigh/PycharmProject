#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************

INF = 999999
def find_cheapest_path(n, m, flights):
    vis = [0]*n
    dis = [0]*n
    # map = [[{'nd':[-1,INF],'d':[-1,INF]}]*n]*n
    ma = [INF]*n
    map = []
    for i in range(n):
        map.append(ma)
    print map
    for f in flights:
        print f[0],f[1]
        map[f[0]][f[1]] = f[3]
        map[f[1]][f[0]] = f[3]
        print map
        # map[f[0]][f[1]]['nd'][0] = f[2]
        # map[f[1]][f[0]]['nd'][1] = f[3]
        # map[f[0]][f[1]]['d'][0] = f[2]
        # map[f[1]][f[0]]['d'][1] = INF
        # map[f[1]][f[0]]['nd'][0] = f[2]
        # map[f[0]][f[1]]['nd'][1] = f[3]
        # map[f[1]][f[0]]['d'][0] = f[2]
        # map[f[0]][f[1]]['d'][1] = INF
    print map
    for i in range(n):
        vis[i] = 0
        if i == 0:
            dis[i] = 0
        else:
            dis[i] = INF
        # dis[i] =0 if i == 0 else INF
        for i in range(n):
            minn = INF
            x = INF
            for j in range(n):
                if vis[j]!=1 and dis[j]<=minn :
                    x = j
                    minn = dis[j]
        print x
        for j in range(n):
            y = j
            print x,y,map[x][y]
            dis[y] = min(dis[y],dis[x]+map[x][y])
            print y,dis[y]
    return dis[1]




# ******************************结束写代码******************************


_n = int(raw_input())

_m = int(raw_input())

_flights_rows = 0
_flights_cols = 0
_flights_rows = int(raw_input())
_flights_cols = int(raw_input())

_flights = []
for _flights_i in xrange(_flights_rows):
    _flights_temp = map(int, re.split(r'\s+', raw_input().strip()))
    _flights.append(_flights_temp)
print _flights
res = find_cheapest_path(_n, _m, _flights)

print str(res) + "\n"