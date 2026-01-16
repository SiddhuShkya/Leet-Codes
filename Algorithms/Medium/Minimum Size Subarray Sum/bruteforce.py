
class Solution(object):
    def minSubArrayLen(self, target, nums):
        minLen = len(nums)
        temp = []
        if sum(nums) < target:
            return 0
        for i in range(len(nums)):
            temp = []
            for j in range(i, len(nums)):
                temp.append(nums[j])
                if sum(temp) >= target:
                    minLen = min(minLen, len(temp))
                    break
        return minLen