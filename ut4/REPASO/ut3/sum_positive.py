# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    if len(numbers) == 0:
        return 0
    if numbers[0] > 0:
        return numbers[0] + run(numbers[1:])
    return run(numbers[1:])


if __name__ == '__main__':
    run([1, -4, 7, 12])