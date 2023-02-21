# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    cascading = []
    while len(values) >= size:
        cascading.append(values[:size])
        del values[0]

    return cascading


if __name__ == "__main__":
    run([1, 2, 3, 4], 3)
