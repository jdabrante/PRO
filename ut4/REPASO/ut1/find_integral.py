# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
    coeff, exponent = symbol.split(",")
    exponent = int(exponent) + 1
    coeff = int(coeff)//exponent
    return f'{coeff}x^{exponent}'


if __name__ == '__main__':
    run('3,2')