def singleElement(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        arr.sort()
        for i in range(0, len(arr), 3):
            if arr[i] in arr[i+1:]:
                continue
            else:
                return arr[i]


print(singleElement([0, 1, 0, 1, 0, 1, 99]))
