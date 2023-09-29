
def jump(nums):
    if canJump(nums):
        count = 0
        l = r = 0
        while r < len(nums) - 1:
            f = 0
            for i in range(l, r+1):
                f = max(f, i + nums[i])
            l = r + 1
            r = f
            count += 1
        return count
    return 0


def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 1, - 1, -1):
        if i + nums[i] >= goal:
            goal = i

    if goal == 0:
        return True
    return False


print(jump([2, 3, 1, 1, 4]))
