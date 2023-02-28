# *******************
# GENERANDO CUADRADOS
# *******************


def gen_sq(n: int) -> list:
    squared = (i**2 for i in range(n))
    return list(squared)
