class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                # We are in the ascending part, peak is to the right
                left = mid + 1
            else:
                # We are in the descending part or at peak
                # peak is at mid or to the left
                right = mid
                
        return left

# Example usage
s = Solution()
print(s.peakIndexInMountainArray([0,1,0]))
print(s.peakIndexInMountainArray([0,2,1,0]))
print(s.peakIndexInMountainArray([0,10,5,2]))
