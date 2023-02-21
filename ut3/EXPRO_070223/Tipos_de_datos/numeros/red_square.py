# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    # TU C�DIGO AQU�
    PI = 3.1415
    diam = (4*arc_A)/round(PI,2)
    area = (diam**2)/4

    return area


if __name__ == '__main__':
    run(1)