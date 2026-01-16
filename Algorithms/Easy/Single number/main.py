def singleNumber(arr):
    if len(arr) == 1:
        return arr[0]
    arr.sort()
    for i in range(0, len(arr), 2):
        if arr[i] in arr[i+1:]:
            continue
        else:
            return arr[i]


print(singleNumber([1, 2, 1, 2, 3]))
