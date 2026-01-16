class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        l = len(arr) - 1
        arr = sorted(arr)
        diff = arr[l] - arr[l-1]
        print(diff)
        for i in range(1, l):
            if arr[i] - arr[i-1] != diff:
                return False
        return True


s = Solution()
print(s.canMakeArithmeticProgression([1,2,4]))