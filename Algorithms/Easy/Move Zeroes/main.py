class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        i = 0
        while i < count:
            for j in range(1, len(nums) - i):
                if nums[j - 1] == 0:
                    temp = nums[j - 1]
                    nums[j - 1] = nums[j]
                    nums[j] = temp
            i += 1
        return nums