# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    powers2 = []
    base = 2
    for number in range(num_powers + 1):
        powers2.append(base**number)
    return powers2


if __name__ == "__main__":
    run(2)
