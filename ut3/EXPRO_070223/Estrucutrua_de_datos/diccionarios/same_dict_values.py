# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    all_same = True
    reference_value = None
    for value in items.values():
        if reference_value is None:
            reference_value = value
        if value != reference_value:
            all_same = False
            break

    return all_same


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})