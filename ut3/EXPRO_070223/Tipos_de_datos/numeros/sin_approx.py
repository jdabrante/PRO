# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
    # TU C�DIGO AQU�
    dividend = 4
    divider = 40500
    angle = 180
    operation = x*(angle - x)
    sin= dividend*operation/(divider-operation)
    return sin


if __name__ == '__main__':
    run(90)