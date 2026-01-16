
def findMode(root):
    if not root:
        return []
    modes = []
    stack = []
    count = {}
    max_count = 0
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if current.val not in count:
            count[current.val] = 1
        else:
            count[current.val] = count[current.val] + 1
        max_count = max(max_count, count[current.val])
        current = current.right

    for key, value in count.items():
        if value == max_count:
            modes.append(key)

    return modes
        

