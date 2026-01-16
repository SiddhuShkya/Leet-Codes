
class Solution(object):
    def merge(self, intervals):
        res = []
        mx, mn = self.findm(intervals)
        print(mx, mn)

    def findm(self, intervals):
        mx = max(intervals[0])
        mn = min(intervals[0])
        for interval in intervals:
            if interval[0] < mn:
                mn = interval[0]
            if interval[1] > mx:
                mx = interval[1]
        return mx, mn

o = Solution()
o.merge(intervals=[[1,3],[2,6],[8,10],[15,18]])