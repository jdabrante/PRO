# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    to_bin = []
    while num >= 1:
        to_bin.append(str(num % 2))
        num //= 2
    to_bin = "".join(list(reversed(to_bin)))
    return to_bin


if __name__ == "__main__":
    run(1)
