def findTheMax(a):
    l = 0

    r = len(a) - 1
    while l < r:

        mid = (l + r) / 2
        # #print l, r, mid,a[l],a[mid],a[r]
        if r - l == 1 and a[l] < a[r]:
            return r
        if a[l] < a[mid]:
            l = mid
            continue
        else:
            r = mid
    return l


def findTheIndex(k, a, maxI):
    ans = -1
    #print 'a',findMidIndex(k, a[0:maxI + 1])
    # #print 'b',findMidIndex(k, a[maxI + 1:]) + maxI
    ans = findMidIndex(k, a[0:maxI + 1])
    if ans == -1 and maxI != len(a)-1:
        ans = findMidIndex(k, a[maxI + 1:]) + maxI+1
    return ans
    # return True

def findMidIndex(k, a):
    #print a
    l = 0
    r = len(a) - 1
    if a[l] == k:
        return l
    while l < r:
        mid = (l + r) / 2
        #print l,mid,r,a[l],a[mid],a[r]

        if a[mid] == k:
            # #print a[mid],k
            return mid
        if a[l] == k:
            return l
        if a[r] == k:
            return r
        if a[mid] < k:
            l = mid
        if a[mid] > k:
            r = mid
    return -1

k = 5
a = [10,5,6,7,8]
max_a_index = findTheMax(a)
# #print 'max_a_index',max_a_index
ans = -1
ans = findTheIndex(k, a, max_a_index)

print ans








