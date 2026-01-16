
def missingNumber(nums):
    nums.append(-1)
    for i in range(len(nums)):
        if i not in nums:
            return i

    # n = len(nums)
    # r = set(range(0, n + 1))
    # return list(r - set(nums))[0]

print(missingNumber([3, 0, 1]))
    