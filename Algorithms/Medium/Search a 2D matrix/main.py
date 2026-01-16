class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1  # Start from the top-right corner of the matrix
        
        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1  # Move down if the current value is less than the target
            else:
                c -= 1  # Move left if the current value is greater than the target
        
        return False




        