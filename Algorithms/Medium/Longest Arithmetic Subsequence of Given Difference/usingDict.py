def longestSubsequence(arr, difference):
    n = len(arr)
    dp = {}
    res = 0
    for num in arr:
        target = num - difference
        if target not in dp:
            dp[num] = 1
        else:
            dp[num] = 1 + dp[target]
        res = max(res, dp[num]);
    return res

print(longestSubsequence([1,5,7,8,5,3,4,2,1], -2))