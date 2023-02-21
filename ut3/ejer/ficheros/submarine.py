# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:
    distance = depth = fuel = 0
    with open(route_path) as f:
        fuel = int(f.readline().strip())
        route = f.read().split(",")
        for direction in route:
            direction = direction.strip().split(":")
            if (fuel - abs(int(direction[0])*3)) < 0:
                break
            distance += int(direction[0])
            depth += int(direction[1])
            fuel -= abs(int(direction[0])*3)
            if depth < 0 or depth > 600:
                break

            

    return distance, depth, fuel


if __name__ == '__main__':
    run('data/submarine/route3.dat')