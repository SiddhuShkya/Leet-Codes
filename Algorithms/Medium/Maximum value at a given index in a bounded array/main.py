def maxValue(n, index, maxSum):
    l = 1
    r = maxSum
    while l < r:
        mid = l + (r-l+1)//2
        if isValid(mid, index, n, maxSum):
            l = mid
        else:
            r = mid - 1
    return l


def isValid(mid, index, n, maxSum):
    total = accumulate(mid)
    leftlength = index + 1
    rightlength = n - index
    leftOffSet = rightOffSet = 0
    if leftlength < mid:
        leftOffSet = -accumulate(mid-leftlength)
    else:
        leftOffSet = leftlength - mid

    if rightlength < mid:
        rightOffSet = -accumulate(mid-rightlength)
    else:
        rightOffSet = rightlength - mid

    ans = total + leftOffSet + total + rightOffSet - mid
    return ans <= maxSum


def accumulate(n):
    return n*(n+1)//2


print(maxValue(4, 2, 6))
