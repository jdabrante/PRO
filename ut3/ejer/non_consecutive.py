"""
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
"""


def run(values: list) -> int:
    last_value = 0
    for i in range(len(values) - 1):
        target = values[i]
        last_value = target[i - 1]
        if target == last_value - 1:
            target = None
        else:
            break
    return target


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
