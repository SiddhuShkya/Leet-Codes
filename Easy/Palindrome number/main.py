
def isPalindrome(x):
    strX = str(x)
    if str(x) == strX[::-1]:
        return True
    else:
        return False


print(isPalindrome(12321))
