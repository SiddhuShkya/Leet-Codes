
def nextPermutation(nums):
    l = len(nums)
    if l <= 2:
        return nums[::-1]
    pointer = l - 2
    while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
        pointer -= 1
    if pointer == -1:
        return nums[::-1]
    for i in range(l-1, pointer, -1):
        if nums[pointer] < nums[i]:
            nums[pointer], nums[i] = nums[i], nums[pointer]
            break
    nums[pointer+1:] = nums[pointer+1:][::-1]
    return nums


print(nextPermutation([5, 4, 3, 2, 1]))
