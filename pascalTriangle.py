def pascalTriangle(n):
    triangle = []
    if n < 1:
        return triangle
    if n == 1:
        triangle.append([1])
        return triangle
    triangle = [[1], [1, 1]]
    for i in range(1, n - 1):
        new_row = [1]
        for j in range(len(triangle[i]) - 1):
            new_row.append(triangle[i][j] + triangle[i][j + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle


print(pascalTriangle(0))
print(pascalTriangle(1))
print(pascalTriangle(2))
print(pascalTriangle(3))
print(pascalTriangle(4))
print(pascalTriangle(100))