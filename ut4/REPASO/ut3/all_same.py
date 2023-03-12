# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    if len(set(items)) == 1:
        return True
    return False
if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])