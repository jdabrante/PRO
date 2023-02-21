# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    # TU CÓDIGO AQUÍ
    csum = []
    rows_values = []
    index = 0
    with open(data_path) as f:
        for line in f:
            row_number = []
            stripped_line = line.strip().split()
            for number in stripped_line:
                row_number.append(int(number))
            rows_values.append(row_number)
        column_numbers = {}
        for value in rows_values:
            for i, number in enumerate(value):
                if not i in column_numbers:
                    column_numbers[i] = number
                else:
                    column_numbers[i] += number
        for column_result in column_numbers.values():
            csum.append(column_result)
        csum = tuple(csum)

    return csum


if __name__ == "__main__":
    run("data/sum_cols/data1.txt")
