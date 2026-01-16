def lengthOfLastWord(s):
    count = 1
    for i in range(1, len(s)):
        if s[-i] == ' ':
            continue
        if s[-(i+1)] != ' ':
            count += 1
        else:
            break
    return count


print(lengthOfLastWord('siddhu shakya'))
