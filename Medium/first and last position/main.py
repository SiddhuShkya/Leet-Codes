
def searchFirst(arr, target, start_idx, last_idx):
    while start_idx <= last_idx:
        mid_idx = (start_idx+last_idx)//2
        if mid_idx == 0 and arr[mid_idx] == target:
            return 0
        if arr[mid_idx] == target and arr[mid_idx-1] < target:
            return mid_idx
        elif arr[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            last_idx = mid_idx - 1
    return - 1


def searchLast(arr, target, start_idx, last_idx):
    while start_idx <= last_idx:
        mid_idx = (start_idx+last_idx)//2
        if mid_idx == len(arr) - 1 and arr[mid_idx] == target:
            return len(arr) - 1
        if arr[mid_idx] == target and arr[mid_idx+1] > target:
            return mid_idx
        elif arr[mid_idx] > target:
            last_idx = mid_idx - 1
        else:
            start_idx = mid_idx + 1
    return - 1


def searchRange(arr, target):
    start_idx = 0
    last_idx = len(arr) - 1
    a = searchFirst(arr, target, start_idx, last_idx)
    b = searchLast(arr, target, start_idx, last_idx)
    return [a, b]


print(searchRange([1, 2, 3, 4, 4, 4, 5, 5, 7, 7, 8, 9, 10, 11, 11], 7))
