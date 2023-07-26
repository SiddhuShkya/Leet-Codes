class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = l + (r-l) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid] > arr[mid - 1]:
                l = mid + 1
            elif arr[mid + 1] < arr[mid] < arr[mid - 1]:
                r = mid

print(Solution().peakIndexInMountainArray([3,9,8,6,4]))
