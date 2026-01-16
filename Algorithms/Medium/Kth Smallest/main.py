def kthSmallest(matrix, k):
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            l.append(matrix[i][j])
    sortedList = sorted(l)
    return sortedList[k-1]


print(kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
