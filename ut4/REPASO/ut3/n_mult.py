# ********************
# CALCULANDO M�LTIPLOS
# ********************


def run(x: int, n: int, multiplies: list = None) -> list:
    if multiplies == None:
        multiplies = []
    if n == 1:
        multiplies.append(x)
        return sorted(multiplies)
    multiplies.append(x * n)
    return run(x, n-1, multiplies)


if __name__ == '__main__':
    run(1, 10)