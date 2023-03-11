# *********************
# VOLUMEN DE UNA ESFERA
# *********************


def run(radius: float) -> float:
    PI = 3.1415
    volume = 4/3*round(PI,2)*radius**3
    return volume
if __name__ == '__main__':
    run(5)