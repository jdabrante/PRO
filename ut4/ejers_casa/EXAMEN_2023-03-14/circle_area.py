# ******************
# �REA DE UN C�RCULO
# ******************


def run(radius: float) -> float:
    PI = 3.1415
    area = round(PI,2)*radius**2
    return area
if __name__ == '__main__':
    run(4)