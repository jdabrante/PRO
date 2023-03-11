# *************************
# LA MULTIPLICACI�N DE JACK
# *************************


def run(n: int) -> int:
    digits = len(str(abs(n)))
    result = n*5**digits
    return result
if __name__ == '__main__':
    run(3)