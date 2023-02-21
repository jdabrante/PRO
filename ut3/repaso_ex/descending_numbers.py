# ****************
# CONTEO REGRESIVO
# ****************


def run(n: int) -> list:
    rev_nums = []
    for number in range(1, n + 1):
        rev_nums.append(number)
    rev_nums.reverse()
    return rev_nums


if __name__ == "__main__":
    run(5)
