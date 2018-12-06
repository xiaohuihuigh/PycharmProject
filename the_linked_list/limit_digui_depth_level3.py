#coding:utf-8
'''
max digui depth is 999
if we limit the depth :500
time fuzadu:
n + t * 500
t is the times you pause the digui

but if the degui too depth you get an error like "the maximum recursion depth exceeded"
'''

def solve(numlist):
    depth_nums = [0]*len(numlist)
    def set_s():
        s = [0]
        def depth(t):
            s[0] += 1
            if s[0] > 500:
                return -1000000
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

if __name__ == '__main__':
    n = raw_input()
    # strnumliststr = raw_input()
    # strnumlist = strnumliststr.split(' ')
    # numlist = [int(i) for i in strnumlist]
    numlist = [i+1 for i in range(int(n)-1)]
    numlist.append(-1)
    #
    # numlist = [i-1 for i in range(int(n))]
    # print numlist
    maxdepth = 0
    so = solve(numlist)
    for t  in range(int(n)/500 + 1):
        for num in range(int(n)):
            t = so[1]()
            depthnum = t[1](num)
            print num,depthnum,t[0]()
            maxdepth = max(maxdepth,depthnum)
    print maxdepth
    # print so[0]()

#我们发现这样会导致一个问题：这个问题是我们会做很多的重复操作，而这些重复操作是没有必要的。