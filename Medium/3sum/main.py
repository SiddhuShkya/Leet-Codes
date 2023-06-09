def threeSum(arr):
    result = []
    arr.sort()
    for idx, a in enumerate(arr):
        if idx > 0 and a == arr[idx-1]:
            continue

        l = idx+1
        r = len(arr)-1
        while l < r:
            three_Sum = a + arr[l] + arr[r]
            if three_Sum > 0:
                r -= 1
            elif three_Sum < 0:
                l += 1
            else:
                result.append([a, arr[l], arr[r]])
                l += 1
                while arr[l] == arr[l-1] and l < r:
                    l += 1
    return result


print(threeSum([-3, -3, 4, -3, 1, 2]))
