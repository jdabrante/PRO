# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    full_value = values1 + values2
    merged = []
    for value in full_value:
        if value not in merged:
            merged.append(value)

    if merged != []:
        max_value = full_value[0]

        for i, value in enumerate(merged):
            if value >= max_value:
                max_value = value
            else:
                if value < max_value:
                    merged.insert(i - 1, value)
                    del merged[i + 1]

    return merged


if __name__ == "__main__":
    run([2, 3, 4, 1], [])
    