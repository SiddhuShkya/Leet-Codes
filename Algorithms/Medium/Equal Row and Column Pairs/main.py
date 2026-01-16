class Solution(object):
    def equalPairs(self, grid):
        res = 0
        cols = []
        for i in range(len(grid)):
            col = []            
            for j in range(len(grid[i])):
                col.append(grid[j][i])
            cols.append(col)
        for row in grid:
            for col in cols:
                if row == col:
                    res += 1
        return res

print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))