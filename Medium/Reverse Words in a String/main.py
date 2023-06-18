class Solution(object):
    def reverseWords(self, s):
        res = ""
        i = len(s) - 1
        while i >= 0:
            word = ""
            while i >= 0 and s[i] == " ":
                i -= 1
            while i >= 0 and s[i] != " ":
                word += s[i]
                i -= 1
            if word:
                res += word[::-1] + " "
        res = self.removeSpace(res)
        return res

    def removeSpace(self, s):
        start = 0
        end = len(s) - 1

        while start <= end and s[start] == " ":
            start += 1

        while end >= start and s[end] == " ":
            end -= 1
        return s[start : end + 1]

print(Solution().reverseWords("the sky is blue"))