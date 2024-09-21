class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        numbers = list(range(1, n+1))
        numbers.sort(key=str)
        return numbers
    

obj = Solution()
print(obj.lexicalOrder(15))