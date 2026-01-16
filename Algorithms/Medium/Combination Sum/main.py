
def combinationSum(candidates, target):
    res = []
    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:])
            return
        if i >= len(candidates) or total > target:
            return
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)
    dfs(0, [], 0)
    return res

print(combinationSum([2,3,6,7], 7))
