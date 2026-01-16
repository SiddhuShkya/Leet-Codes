class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r, c):
            if (r == ROWS or c == COLS or not matrix[r][c]):
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
             
            cache[(r, c)] = 1 + min(
                dfs(r + 1, c),
                dfs(r, c + 1),
                dfs(r + 1, c + 1)
            )
            return cache[(r, c)]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += dfs(r, c)

        return res
        
        


matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

o = Solution()
print(o.countSquares(matrix=matrix))