def plusOne(digits):
    newStr = ''
    result = []
    for i in range(len(digits)):
        newStr += str(digits[i])
    resultStr = str(int(newStr) + 1)
    for j in range(len(resultStr)):
        result.append(int(resultStr[j]))
    return result


print(plusOne([123]))
