class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub