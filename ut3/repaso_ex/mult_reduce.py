# ************************
# MULTIPLICACIÓN EN CADENA
# ************************


def run(numbers: list) -> int:
    rmult = 1
    numbers.sort()

    for number in numbers:
        rmult *= number
    return rmult


if __name__ == "__main__":
    run([1, 5, 2, 1])
