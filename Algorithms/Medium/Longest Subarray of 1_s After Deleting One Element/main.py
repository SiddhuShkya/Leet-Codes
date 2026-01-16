class Solution(object):
    def longestSubarray(self, nums):
        res = 0
        curr = 0
        prev = 0
        if 0 in nums:
            for num in nums:
                if num == 1:
                    curr += 1
                else:
                    res = max(res, curr + prev)
                    prev = curr
                    curr = 0
            res = max(res, curr+prev)
            return res
        else:
            return len(nums) - 1


print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))