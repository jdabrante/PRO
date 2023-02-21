# *********************
# ¿QUÉ ES LO SIGUIENTE?
# *********************


def run(items: list, ref_item: object) -> object:
    target_item = None
    if ref_item in items and (items.index(ref_item) < len(items) - 1):
        index = items.index(ref_item)
        target_item = items[index + 1]

    return target_item


if __name__ == "__main__":
    run([1, 2, 3, 4, 5, 6, 7], 3)
