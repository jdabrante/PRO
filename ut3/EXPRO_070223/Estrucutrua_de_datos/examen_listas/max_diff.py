# ***************************
# BUSCANDO LA MAYOR DISTANCIA
# ***************************


def run(values: list, target: int) -> int:
    # TU C�DIGO AQU�
    max_diff = 0
    for value in values:
        difference = abs(target - value)
        if difference > max_diff:
            max_diff = difference
    return max_diff


if __name__ == '__main__':
    run([7, 3, 1, 12, 21, 4], 8)