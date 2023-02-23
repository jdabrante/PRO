# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    items_list = [(letter, number) for letter, number in unsorted_items.items()]
    sorted_items = sorted(items_list, key=lambda t: t[1])

    return sorted_items


if __name__ == "__main__":
    run({"a": "two", "b": "one", "c": "three"})
