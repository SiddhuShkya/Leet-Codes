class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            sub = []
            for j in range(i+1):
                if j == 0 or j == i:
                    sub.append(1)
                else:
                    prev_row = res[i - 1]
                    num = prev_row[j - 1] + prev_row[j]
                    sub.append(num)
            res.append(sub)
        return res

s = Solution()
print(s.generate(5))