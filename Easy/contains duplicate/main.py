
def containsDuplicate(nums):
    s = set(nums)
    if len(s) != len(nums):
        return True
    return False


print(containsDuplicate([1, 7, 3, 9, 2, 3]))
