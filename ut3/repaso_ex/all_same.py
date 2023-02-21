# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************

# Forma 1
# =============================

# def run(items: list) -> bool:
#     if items.count(items[0]) == len(items):
#         all_same = True
#     else:
#         all_same = False
#     return all_same


# if __name__ == "__main__":
#     run([1, 1, 1, 1, 1, 1])

# =============================

# Forma 2
# =============================
def run(items: list) -> bool:
    last_item = items[0]
    for item in items:
        if item == last_item:
            last_item = item
        else:
            all_same = False
            break
    else:
        all_same = True
    return all_same


if __name__ == "__main__":
    run([1, 1, 1, 1, 1, 1])
