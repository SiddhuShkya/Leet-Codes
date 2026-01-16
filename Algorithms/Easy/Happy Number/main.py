import math

class Solution(object):
    def isHappy(self, n):
        tmp = math.pow(n, 2)
        seen_numbers = set()
        while True:
            total = 0
            while (n > 0):
                dt = n%10
                total += math.pow(dt, 2)
                n = n//10
            if total == 1:
                return True
            if total in seen_numbers:
                return False
            seen_numbers.add(total)
            n = total
        

o = Solution()
print(o.isHappy(n=7))