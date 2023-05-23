# Brue force
def twoSum_Bruteforce(arr, target):
    # nested loop = O(n x n) = O(n^2)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j] == target):
                return [i, j]
    return "Such sum does not exist in the array"


print(twoSum_Bruteforce([10, 11, 3, 15, 6], 9))

# T(n) = o(n^2)


def twoSum_hashmap(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[nums[i]] = i


print(twoSum_hashmap([10, 11, 3, 15, 6], 9))

# T(n) = O(n)
