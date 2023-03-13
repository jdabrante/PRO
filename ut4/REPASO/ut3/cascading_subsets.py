# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    cascading = []
    for i in range(len(values)):
        if len(values[i:size+i]) == size:
            cascading.append(values[i:size+i])
    return cascading


if __name__ == '__main__':
    run([1, 2, 3, 4], 3)