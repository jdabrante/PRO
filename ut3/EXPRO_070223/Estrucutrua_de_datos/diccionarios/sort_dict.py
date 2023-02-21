# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    sorted_items = []
    matrix = []
    for key,value in unsorted_items.items():
        new = [value,key]
        matrix.append(new)
    matrix.sort()
    for value in matrix:
        new_value = value[::-1]
        new_value = tuple(new_value)
        sorted_items.append(new_value)
    return sorted_items


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})