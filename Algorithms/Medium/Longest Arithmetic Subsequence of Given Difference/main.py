def longestSubsequence(arr, difference):
    max_len = 1
    for i in range(len(arr)):
        l = arr[i]
        subs = [l]
        for j in range(i + 1, len(arr)):
            if (arr[j] - l == difference):
                subs.append(arr[j])
                l = arr[j]
        max_len = max(max_len, len(subs))
    return max_len

print(longestSubsequence([1,5,7,8,5,3,4,2,1], -2))