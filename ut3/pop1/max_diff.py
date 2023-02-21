# ***************************
# BUSCANDO LA MAYOR DISTANCIA
# ***************************


def run(values: list, target: int) -> int:
    max_diff = 0
    if values != []:
        max_diff = abs(values[0] - target)
        for value in values:
            if max_diff < abs(value - target):
                max_diff = abs(value - target)
    return max_diff


if __name__ == "__main__":
    run([-5, -9, 12, 18], 15)
