
def search_insert_position(arr, target):
    low_idx = 0
    high_idx = len(arr)-1
    while low_idx <= high_idx:
        mid_idx = (high_idx+low_idx)//2
        if arr[mid_idx] == target:
            return mid_idx
        else:
            if arr[mid_idx] < target:
                low_idx = mid_idx + 1
            else:
                high_idx = mid_idx - 1
    return low_idx


print(search_insert_position([1, 3, 5, 6], 4))
