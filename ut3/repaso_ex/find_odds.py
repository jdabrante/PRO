# ********************
# DESCUBRIENDO IMPARES
# ********************


def run(values: list) -> list:
    odds = []
    # [odds.append(value) for value in values if value not in odds and value % 2 != 0]

    for value in values:
        if (value not in odds) and (value % 2 == 1):
            odds.append(value)

    return odds


if __name__ == "__main__":
    run([1, 2, 3, 4, 5])
