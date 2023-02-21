# ********************
# CALCULANDO MÚLTIPLOS
# ********************


def run(x: int, n: int) -> list:
    multiples = []
    for number in list(range(1, n + 1)):
        multiples.append(number * x)
    return multiples


if __name__ == "__main__":
    run(1, 10)
