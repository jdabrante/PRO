# ******************
# DISTANCIA EUCL�DEA
# ******************


def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # TU C�DIGO AQU�
    first = (x1-x2)**2
    second = (y1-y2)**2
    distance = (first+second)**0.5

    return distance


if __name__ == '__main__':
    run(3, 5, -7, -4)