# ***************************
# DICCIONARIO EN CONSTRUCCI�N
# ***************************


def run(items: list) -> dict:
    # TU C�DIGO AQU�
    #desempaquetado el for key, *values in items
    unpack_items = {key: values for key, *values in items}
    return unpack_items


if __name__ == '__main__':
    run([['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'], ['Episode V - The Empire Strikes Back', 'May 21', 1980], ['Episode VI - Return of the Jedi', 'May 25', 1983]])