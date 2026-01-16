
def isPalindrome(s):
    s = s.lower()
    letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    newStr = ''
    for char in s:
        if char in letterList or char in numList:
            newStr += char
    if newStr == newStr[::-1]:
        return True
    return False


print(isPalindrome('racecar'))
