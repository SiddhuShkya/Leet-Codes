
def longestCommonSubsequence(text1, text2):
    l1, l2 = len(text1), len(text2)
    if text1 == text2:
        return l1
    dp = [[ 0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]

print(longestCommonSubsequence("abcde", "ace"))