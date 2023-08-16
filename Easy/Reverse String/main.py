class Solution(object):
    def reverseString(self, s):
        l = len(s) - 1
        i = 0
        while (i != l and i < l):
            s[i], s[l] = s[l], s[i]
            l -= 1
            i += 1
        return s