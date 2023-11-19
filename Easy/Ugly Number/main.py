def isUgly(n):
    if n < 1:
        return False
    for p in [2, 3, 5]:
        while n%p == 0:
            n = n // p
    return n == 1


print(isUgly(15))