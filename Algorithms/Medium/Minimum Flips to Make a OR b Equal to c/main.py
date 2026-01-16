class Solution(object):
    def minFlips(self, a, b, c):
        flips = 0
        a_bin = self.convertToBin(a)
        b_bin = self.convertToBin(b)
        c_bin = self.convertToBin(c)
        max_len = max(len(a_bin), len(b_bin), len(c_bin))
        a_bin = a_bin.zfill(max_len)
        b_bin = b_bin.zfill(max_len)
        c_bin = c_bin.zfill(max_len)
        for i in range(max_len):
            if c_bin[i] == "0":
                if a_bin[i] == "1" and b_bin[i] == "1":
                    flips += 2
                elif (a_bin[i] == "0" and b_bin[i] == "1") or (a_bin[i] == "1" and b_bin[i] == "0"):
                    flips += 1
            else:
                if a_bin[i] == "0" and b_bin[i] == "0":
                    flips += 1
        return flips

    def convertToBin(self, i):
        if i == 0:
            return '0'
        res = ""
        while i > 0:
            if i % 2 == 0:
                res = "0" + res
            else:
                res = "1" + res
            i = i // 2
        return res


s = Solution()
print(s.minFlips(10, 9, 1))
