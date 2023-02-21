A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

product_00 = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])
product_01 = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
product_10 = (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
product_11 = (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])

row1 = [product_00, product_01]
row2 = [product_10, product_11]

matrix = [[row1], [row2]]
print(matrix)
