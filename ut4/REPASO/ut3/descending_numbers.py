# ****************
# CONTEO REGRESIVO
# ****************


def run(n: int, result: list = None) -> list:
    if result == None:
        result = []
    if n == 1:
        result.append(1)
        return result
    elif n > 1:
        result.append(n)
        run(n-1, result)
        return result
    return result

print(run(1))

if __name__ == '__main__':
    run(1)