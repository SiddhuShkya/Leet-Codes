

def minBitFlips(start, goal):
    res = 0
    while start or goal:
        if (start % 2) != (goal % 2):
            res += 1
        start = start // 2
        goal = goal // 2
    return res

print(minBitFlips(10, 7))