def setZeroes(matrix):
    rows = set()  
    cols = set()  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        for i in range(len(matrix[0])):
            matrix[row][i] = 0

    for col in cols:
        for i in range(len(matrix)):
            matrix[i][col] = 0

    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
