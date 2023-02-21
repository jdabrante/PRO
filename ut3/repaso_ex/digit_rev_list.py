# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    number = list(str(number))
    rev_digits_str = number[::-1]
    rev_digits = []
    for digits in rev_digits_str:
        rev_digits.append(int(digits))
    return rev_digits


if __name__ == "__main__":
    run(35231)
