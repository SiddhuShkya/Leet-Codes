def kWeakestRows(mat, k):
    res = list()
    counts = dict()
    for i in range(len(mat)):
        counts[i] = sum(mat[i])
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1]))
    for count in list(sorted_counts.keys())[:k]:
        res.append(count)
    return res

print(kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))