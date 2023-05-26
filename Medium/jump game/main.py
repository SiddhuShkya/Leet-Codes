
def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 1, - 1, -1):
        if i + nums[i] >= goal:
            goal = i

    if goal == 0:
        return True
    return False


print(canJump([3, 2, 1, 0, 4]))
