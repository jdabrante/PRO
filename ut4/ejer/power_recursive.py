# ******************
# POTENCIA RECURSIVA
# ******************


def power(x: int, n: int) -> int:
    count += 1
    result *= x

    if count == n:
        return result
    return power(x, n, count, result)
