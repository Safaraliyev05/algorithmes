def generate_spiral_matrix(m, n):
    matrix = [[0] * n for _ in range(m)]

    left, right, top, bottom = 0, n - 1, 0, m - 1
    num = 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


m, n = 4, 4  # Change these values as needed
matrix = generate_spiral_matrix(m, n)
for row in matrix:
    print(row)
