
def getLastMoment(n, left, right):
    plank_left = (n+1) * ["_"]
    plank_right = (n+1) * ["_"]
    for i in left:
        plank_left[i] = "a"
    for i in right:
        plank_right[i] = "a"
    tl = 0
    tr = 0
    # for left
    for i in range(len(plank_left) - 1, -1, -1):
        if plank_left[i] == "a":
            tl = max(tl, len(plank_left[:i]))
            break
    # for right
    for i in range(len(plank_right)):
        if plank_right[i] == "a":
            tr = max(tr, len(plank_right[i + 1:]))
            break
    return max(tl, tr)

print(getLastMoment(4, [4, 3], [0,1]))