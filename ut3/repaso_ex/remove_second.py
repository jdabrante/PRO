# *************************
# NO ME INTERESAN LOS PARES
# *************************

# Forma 1
# ==========================
# def run(items: list) -> list:
#     filter = items[::2]
#     return filter
# ==========================


def run(items: list) -> list:
    filter = []
    for i, item in enumerate(items):
        if i % 2 == 0:
            filter.append(item)
    return filter


if __name__ == "__main__":
    run([1, 2, 1, 2, 1, 2])
