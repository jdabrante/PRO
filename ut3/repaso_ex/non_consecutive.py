# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    target = None
    for i in range(1, len(values)):
        if values[i] != values[i - 1] + 1:
            target = values[i]
            break
    return target


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
