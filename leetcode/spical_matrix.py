def spiral_matrix(n, m):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        result.append(row)
    return result


print(spiral_matrix(2, 3))
print(spiral_matrix(2, 4))
