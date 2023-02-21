# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:
    # TU CÓDIGO AQUÍ
    distance = depth = fuel = 0
    with open(route_path) as f:
        fuel = int((f.readline()).strip())
        directions = (f.readline()).strip()
        directions = directions.split(",")
        separate_directions = []
        for direction in directions:
            direction = direction.split(":")
            separate_directions.append(direction)
        for x,y in separate_directions:
            x = int(x)
            y = int(y)
            if fuel > 0:
                fuel -= abs(x)*3
                distance += x
                depth += y
            if depth < 0 or depth > 600:
                break
            
    return distance, depth, fuel


if __name__ == '__main__':
    run('data/submarine/route1.dat')