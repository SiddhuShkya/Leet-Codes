def countNicePairs(nums):
    d = {}
    for i in range(len(nums)):
        diff = nums[i] - rev(nums[i])
        if diff not in d:
            d[diff] = 1
        else:
            d[diff] += 1
    res = 0
    for i in d.values():
        res = res + (i*(i - 1)//2)
    return res%(10**9 + 7)
    

def rev(num):
    res = 0
    while num != 0:
        res = res * 10 + num % 10
        num //= 10
    return res

print(countNicePairs([42, 11, 1, 97]))