# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    result = [items[0]]
    control_num = items[0]
    for item in items:
        if item != control_num:
            result.append(item)
            control_num = item
    return result


if __name__ == "__main__":
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
