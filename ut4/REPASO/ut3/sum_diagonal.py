# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    matrix_len = len(matrix)
    sum_diagonal = sum([matrix[i][j] for i in range(matrix_len) for j in range(matrix_len) if i==j])
    return sum_diagonal


if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])