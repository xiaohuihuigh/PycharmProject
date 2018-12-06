#O(n)
if __name__ == '__main__':
    # digui_main()
    n = raw_input()
    strnumliststr = raw_input()
    strnumlist = strnumliststr.split(' ')
    numlist = [int(i) for i in strnumlist]
    #
    # numlist = [i+1 for i in range(int(n)-1)]
    numlist.append(-1)
    depth_nums = [0]*int(n)
    # numlist = [i - 1 for i in range(int(n))]
    print numlist
    maxdepth = 0
    for num in range(int(n)):
        tnum = num
        if depth_nums[tnum] != 0:
            continue
        depth_nums[tnum] = 1
        while 1:
            if numlist[tnum] != -1:
                if depth_nums[numlist[tnum]] >= depth_nums[tnum]+1:
                    maxdepth = maxdepth + depth_nums[numlist[tnum]] - 1 - depth_nums[tnum]
                    break
                depth_nums[numlist[tnum]] = depth_nums[tnum]+1
                tnum = numlist[tnum]
            elif numlist[tnum] == -1:
                maxdepth = depth_nums[tnum]
                break
    print maxdepth