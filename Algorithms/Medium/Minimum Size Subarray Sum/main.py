
def minSubArrayLen(target, nums):  
    minLen = float('inf') 
    currentSum = 0
    start = 0
    for end in range(len(nums)):
        currentSum += nums[end]
        while currentSum >= target:
            minLen = min(minLen, end - start + 1)
            currentSum -= nums[start]
            start += 1
    return minLen if minLen != float('inf') else 0    

print(minSubArrayLen(7, [2,3,1,2,4,3]))
    