# ************************
# MULTIPLICACI�N EN CADENA
# ************************


def run(numbers: list) -> int:
    if len(numbers) == 0:
        return 1
    return numbers[0] * run(numbers[1:])


if __name__ == '__main__':
    run([1, 2, 3, 4])