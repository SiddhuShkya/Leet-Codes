class Solution(object):
    def distributeCookies(self, cookies, k):
        count = [0] * k
        res = [float("inf")] 
        self.backTrack(0, cookies, k, count, res)
        if res[0] == float("inf"):
            return None  
        return res[0]


    def backTrack(self, cookieNumber, cookies, k, count, res):
        if cookieNumber == len(cookies):
            mx = max(count)
            res[0] = min(res[0], mx)
            return
        for i in range(k):
            count[i] += cookies[cookieNumber]
            self.backTrack(cookieNumber + 1, cookies, k, count, res)
            count[i] -= cookies[cookieNumber]
            if count[i] == 0:
                break

print(Solution().distributeCookies([8, 15, 10, 20, 8], 2))
