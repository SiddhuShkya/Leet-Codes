class Solution(object):
    def peakIndexInMountainArray(self, arr):
        peak = 0
        for i in range(len(arr)):
            if arr[i] > peak:
                peak = arr[i]
            if arr[i] < peak:
                return i - 1
        return


print(Solution().peakIndexInMountainArray([0,1,0]))