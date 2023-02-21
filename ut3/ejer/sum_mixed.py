"""
Dada una lista de enteros y enteros como cadenas de texto, calcule la suma de todos los
valores de la lista como si todos sus elementos fueran números.
"""


def run(items: list) -> int:
    items_int = []
    for item in items:
        if type(item) != int:
            value_int = int(item)
            items_int.append(value_int)
        else:
            items_int.append(item)
    sum_items = sum(items_int)
    return sum_items
