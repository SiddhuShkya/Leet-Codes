
def countConsistentStrings(allowed, words):
    res = 0
    for item in words:
        ln = 0
        for char in item:
            if char not in allowed:
                break
            else:
                ln += 1
        if ln == len(item):
            res += 1
    return res

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))