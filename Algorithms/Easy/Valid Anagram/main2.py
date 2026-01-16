def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hash_map = {}
    for c in s:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    for c in t:
        if c in hash_map:
            hash_map[c] -= 1
        else:
            return False
    for c in s:
        if hash_map[c] != 0:
            return False
    return True


print(isAnagram('anagram', 'gramana'))
