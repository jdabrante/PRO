# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    add_inv = sum([number*(-1) for number in numbers ])
    return add_inv
if __name__ == '__main__':
    run([1, 2, 3, 4, 5])