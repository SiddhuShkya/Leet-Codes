
def containsNearbyDuplicate(nums, k):
    n = len(nums)
    s = set(nums)
    if n > len(s):
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap and k >= i - hashMap[nums[i]]:
                return True
            else:
                hashMap[nums[i]] = i
    return False


print(containsNearbyDuplicate([1, 2, 3, 4, 5, 5], 5))
