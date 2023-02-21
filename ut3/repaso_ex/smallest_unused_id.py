# *****************
# MENOR ID SIN USAR
# *****************


def run(ids: list) -> int:

    smallest_list = []
    ids.sort()

    for value in range(1, ids[len(ids) - 1]):
        if value not in ids:
            smallest_list.append(value)

    if smallest_list != []:
        smallest_unused_id = min(smallest_list)
    else:
        smallest_unused_id = smallest_list[len(ids) - 1] + 1

    return smallest_unused_id


if __name__ == "__main__":
    run([7, 2, 12, 21, 5])
