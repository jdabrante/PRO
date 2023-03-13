# ********************
# CUBOIDES Y VOL�MENES
# ********************
volum = lambda c: c[0]*c[1]*c[2]

def decorator(func):
    def wrapper (*args,**kwargs):
        result = abs(func(*args,**kwargs))
        return result
    return wrapper

@decorator
def run(cuboid1: list, cuboid2: list) -> float:
    vol_diff = volum(cuboid1) - volum(cuboid2)
    return vol_diff


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])