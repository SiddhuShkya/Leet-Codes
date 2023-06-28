def longest_prefix(arr):
    prefix = ""
    for i in range(len(arr[0])):
        for s in arr:
            if i == len(s) or arr[0][i] != s[i]:
                return prefix
        prefix += arr[0][i]
    return prefix


print(longest_prefix(["flow", "flower", "flown"]))
