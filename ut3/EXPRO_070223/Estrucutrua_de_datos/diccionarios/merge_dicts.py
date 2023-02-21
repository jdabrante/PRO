# **********************
# MEZCLANDO DICCIONARIOS
# **********************


def run(d1: dict, d2: dict) -> dict:
    # TU C�DIGO AQU�
    merged = d2.copy()
    for key,value in d1.items():
        if key not in d2:
            merged[key] = value
    return merged


if __name__ == '__main__':
    run({'a': 1, 'b': 2}, {'a': 3, 'c': 4})