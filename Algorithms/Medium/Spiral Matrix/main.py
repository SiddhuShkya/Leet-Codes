def spiralOrder(matrix):
    res = []
    if not matrix:
        return res
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    nums = rows * cols
    while nums:
        # Traverse top row
        for j in range(left, right + 1):
            res.append(matrix[top][j])
            nums = nums - 1
        top += 1
        # Traverse right column
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
            nums = nums - 1
        right -= 1
        # Traverse bottom row (if applicable)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
                nums = nums - 1
            bottom -= 1
        # Traverse left column (if applicable)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
                nums = nums - 1
            left += 1
    return res

print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
