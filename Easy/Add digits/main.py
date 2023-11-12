def addDigits(num):
    if num < 10:
        return num
    return addDigits(add(num))

def add(num):
    res = 0
    while num > 0:
        res = num % 10 + res
        num = num // 10
    return res

print(addDigits(38))
