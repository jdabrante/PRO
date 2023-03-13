# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    values1.extend(values2)
    merged = []
    for value in values1: 
        if value not in merged:
            merged.append(value)
    return merged

if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])