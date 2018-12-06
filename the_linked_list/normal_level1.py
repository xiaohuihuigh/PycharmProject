'''
max digui depth is 999
time fuzadu:
1+2+...+n
'''

def solve(numlist):
    s = [0]
    def depth(t):
        s[0] += 1
        # print s[0]
        if numlist[t] == -1:
            return 1
        return depth(numlist[t])+1
    def get_s():
        return s[0]
    return get_s,depth
def digui_main():
    n = raw_input()
    # strnumliststr = raw_input()
    # strnumlist = strnumliststr.split(' ')
    # numlist = [int(i) for i in strnumlist]

    # numlist = [i+1 for i in range(int(n)-1)]
    # numlist.append(-1)

    numlist = [i - 1 for i in range(int(n))]
    print numlist
    maxdepth = 0

    for num in range(int(n)):
        so = solve(numlist)
        depthnum = so[1](num)
        print num, depthnum, so[0]()
        maxdepth = max(maxdepth, depthnum)
    print maxdepth
def zhan_main():
    n = raw_input()
    strnumliststr = raw_input()
    strnumlist = strnumliststr.split(' ')
    numlist = [int(i) for i in strnumlist]

    # numlist = [i+1 for i in range(int(n)-1)]
    # numlist.append(-1)

    # numlist = [i - 1 for i in range(int(n))]
    print numlist
    maxdepth = 0
    maxdepth = 0
    for num in range(int(n)):
        zhan_list = []
        tnum = num
        while 1:
            if tnum != -1:
                zhan_list.append(tnum)
                tnum = numlist[tnum]
            if tnum == -1:
                maxdepth = max(maxdepth,len(zhan_list))
                break
    print maxdepth
if __name__ == '__main__':
    # digui_main()
    zhan_main()