class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        ln = len(strs)
        for i in range(ln):
            sub_res = [strs[i]]
            for j in range(ln):
                if i == j:
                    continue
                if sorted(strs[i]) == sorted(strs[j]):
                    sub_res.append(strs[j])
            sub_res = sorted(sub_res)
            if sub_res not in res:
                res.append(sub_res)
        return res
    
o = Solution()
print(o.groupAnagrams(["a"]))
                    
