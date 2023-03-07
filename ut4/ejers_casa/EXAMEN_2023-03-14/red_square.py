# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    PI = 3.1415
    calc = (arc_A*4)/(2*round(PI,2))
    area = ((calc*2)**2)/4
    return area
if __name__ == '__main__':
    run(1)