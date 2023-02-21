# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    add_inv = 0
    for number in numbers:
        add_inv += number * (-1)
    return add_inv


if __name__ == "__main__":
    run([1, 2, 3, 4, 5])


if __name__ == "__main__":
    run([1, 2, 3, 4, 5])
