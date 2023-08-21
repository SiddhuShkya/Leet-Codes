def repeatedSubstringPattern(s):
    l = len(s)
    for substring_len in range(1, l // 2 + 1):
        if l % substring_len == 0:
            num_repeats = l // substring_len
            substring = s[:substring_len]
            formed_string = substring * num_repeats
            if formed_string == s:
                return True        
    return False

print(repeatedSubstringPattern("abcabc"))
