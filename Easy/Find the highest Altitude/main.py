class Solution(object):
    def largestAltitude(self, gain):
        alt = 0
        res = 0
        n = len(gain)
        for i in range(n):
            alt += gain[i]
            res = max(alt, res)
        return res
    

print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))