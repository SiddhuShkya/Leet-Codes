
def isAnagram(s, t):
    if len(s) == len(t):
        if sorted(s) == sorted(t):
            return True
        return False
    return False


print(isAnagram("anagram", "nagaram"))
