
# 构建一个3行5列的二维list
matrix = [[False for i in range(5)] for j in range(3)]

print(matrix)

print('---------------------------------')

matrix[0][0] = True
matrix[1][1] = True
matrix[2][2] = True
matrix[2][3] = True

print(matrix)
