# *****************
# MENOR ID SIN USAR
# *****************


def run(ids: list) -> int:
    for id in range(1,len(ids)):
        if id not in ids:
            return id
    return len(ids)+1


if __name__ == '__main__':
    run([3, 1, 8, 4, 9])