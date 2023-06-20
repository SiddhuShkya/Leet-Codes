class Solution(object):
    def getAverages(self, nums, k):
        avgs = []
        first_idx = 0
        last_idx = len(nums) - 1
        window_sum = sum(nums[:2*k+1])
        print(sum(nums[:2*k+1]))
        while first_idx <= last_idx:
            if first_idx < k or first_idx > last_idx - k:
                avgs.append(-1)
            else:
                avgs.append(window_sum //(2*k+1)) 
                if first_idx < last_idx - k:
                    print(nums[first_idx - k], nums[first_idx + k + 1])
                    # Update the window sum efficiently
                    window_sum -= nums[first_idx - k]
                    window_sum += nums[first_idx + k + 1]
            first_idx += 1
        return avgs

print(Solution().getAverages([7,4,3,9,1,8,5,2,6], 3))