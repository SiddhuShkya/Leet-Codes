

def isPowerOfFour(n):
    if n == 1:
        return True
    i = 1
    while True:
        if (n == 4**i):
            return True
        if (4**i > n):
            return False
        i += 1


print(isPowerOfFour(16))