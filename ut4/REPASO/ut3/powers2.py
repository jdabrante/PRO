# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int, powers2 = None) -> list:
    if powers2 == None:
        powers2 = [1]
    if num_powers == 0:
        return powers2
    run(num_powers - 1, powers2)
    powers2.append(2**num_powers)
    return powers2


if __name__ == '__main__':
    run(2)