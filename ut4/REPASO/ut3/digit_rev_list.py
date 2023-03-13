# ************************
# D�GITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    rev_digits = list(str(number))
    rev_digits = [int(value) for value in rev_digits]

    return rev_digits


if __name__ == '__main__':
    run(35231)