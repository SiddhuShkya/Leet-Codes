class Solution(object):
    def countNegatives(self, grid):
        res = 0
        for item in grid:
            for i in range(len(item) - 1, -1, -1):
                if item[i] < 0:
                    res += 1
                else:
                    break           
        return res

s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))