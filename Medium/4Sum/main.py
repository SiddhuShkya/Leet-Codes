class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            # Avoid duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # Avoid duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Avoid duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Avoid duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result
    
    
obj = Solution()
print(obj.fourSum([1,0,-1,0,-2,2], 0))