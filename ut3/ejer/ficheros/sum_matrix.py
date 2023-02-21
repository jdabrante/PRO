# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = "data/sum_matrix/result.dat"
    matrix_1 = []
    matrix_2 = []
    result = []
    line_result = []
    index = 0
    
    
    with open(matrix1_path) as f:
        for line in f:
            line_list = line.split()
            matrix_1.append(line_list)

    with open(matrix2_path) as f:
        for line in f:
            line_list = line.split()
            matrix_2.append(line_list)

    with open(result_path, "w") as f:
        for i, values in enumerate(matrix_1):
            for value in values:
                operation = int(matrix_1[i][index]) + int(matrix_2[i][index])
                result.append(str(operation))
                index += 1
            line_result.append(result)
            index = 0
            result = []
        for values in line_result:
            line_values = " ".join(values)
            f.write(f"{line_values}\n")

    return filecmp.cmp(result_path, "data/sum_matrix/.expected", shallow=False)


if __name__ == "__main__":
    run("data/sum_matrix/matrix1.dat", "data/sum_matrix/matrix2.dat")
