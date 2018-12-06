#coding:utf-8
'''
max digui depth is 999
time fuzadu:
n

but if the degui too depth you get an error like "the maximum recursion depth exceeded"
'''

def solve(numlist):
    depth_nums = [0]*len(numlist)
    def set_s():
        s = [0]
        def depth(t):
            s[0] += 1
            # print s[0]
            if depth_nums[t] > 0:
                return depth_nums[t]
            if numlist[t] == -1:
                depth_nums[t] = 1
                return depth_nums[t]
            depth_nums[t] = depth(numlist[t])+1
            return depth_nums[t]
        def get_s():
            return s[0]
        return get_s,depth
    def get_depth_num():
        return depth_nums
    return get_depth_num,set_s
def digui_main():
    n = raw_input()
    # strnumliststr = raw_input()
    # strnumlist = strnumliststr.split(' ')
    # numlist = [int(i) for i in strnumlist]
    numlist = [i + 1 for i in range(int(n) - 1)]
    numlist.append(-1)
    #
    # numlist = [i-1 for i in range(int(n))]
    print numlist
    maxdepth = 0
    so = solve(numlist)
    for num in range(int(n)):
        t = so[1]()
        depthnum = t[1](num)
        print num, depthnum, t[0]()
        maxdepth = max(maxdepth, depthnum)
    print maxdepth
    # print so[0]()
def zhan_main():
    #复杂度是n的，所以已经是最优的结果了。
    n = raw_input()
    strnumliststr = raw_input()
    strnumlist = strnumliststr.split(' ')
    numlist = [int(i) for i in strnumlist]
    # numlist = [i + 1 for i in range(int(n) - 1)]
    # numlist.append(-1)
    #
    # numlist = [i-1 for i in range(int(n))]
    print numlist
    maxdepth = 0
    depth_nums = [0]*int(n)
    for num in range(int(n)):
        zhan_list = []
        tnum = num
        while 1:
            # print zhan_list
            if tnum != -1 and depth_nums[tnum] == 0:
                zhan_list.append(tnum)
                tnum = numlist[tnum]
            elif depth_nums[tnum] !=0:
                depth = depth_nums[tnum]
                zhan_list.reverse()
                for znum in zhan_list:
                    depth_nums[znum] = depth + 1
                    depth += 1
                break
            elif tnum == -1:
                depth = 0
                zhan_list.reverse()
                for znum in zhan_list:
                    depth_nums[znum] = depth + 1
                    depth += 1
                break
    for i in depth_nums:
        maxdepth = max(maxdepth,i)
    print maxdepth

if __name__ == '__main__':
    # digui_main()
    zhan_main()