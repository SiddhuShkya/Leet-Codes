class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        res = 0
        for r in range(len(s)):
            if s[l] != s[r]:
                if r & 1:
                    res += 1
                l = r
        return res
                    
        