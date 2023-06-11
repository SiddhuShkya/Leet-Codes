def remove(nums, val):
    i = 0
    for item in nums:
        if item != val:
            nums[i] = item
            i += 1
    return i


print(remove([0, 1, 2, 3, 3, 5, 3, 9], 3))
