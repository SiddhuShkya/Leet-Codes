

def longestPalindrome(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    if len(d) == 1:
        return len(s)
    odd = 0
    res = 0
    for i in d.values():
        if i > 1:
            if i % 2 == 0:
                res += i
            else:
                res += i - 1
                odd += 1
        else:
            odd += 1

    if odd > 0:
        res += 1
    return res

print(longestPalindrome('abccccdd'))
