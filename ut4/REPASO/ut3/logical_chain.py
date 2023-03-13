# ******************
# CALCULADORA L�GICA
# ******************


def run(values: list, oper: str) -> bool:
    result = 1
    for value in values: 
        if oper == 'and':
            result *= bool(value)
        else:
            result += bool(value) 
    return bool(result)


if __name__ == '__main__':
    run([True, True, False], 'and')