def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums)):
        if (len(nums[i:k+i]) == k):
            res.append(max(nums[i:k+i]))
    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))