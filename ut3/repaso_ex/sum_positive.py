# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    sum_positive = 0
    for number in numbers:
        if number >= 0:
            sum_positive += number
    return sum_positive


if __name__ == "__main__":
    run([1, -4, 7, 12])
