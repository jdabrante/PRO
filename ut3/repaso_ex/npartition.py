# ***********************
# PARTICIÓN POR EL NÚMERO
# ***********************


def run(values: list, ref_value: int) -> list:
    less_reference = []
    equal_greference = []
    npartition = []
    for value in values:
        if value < ref_value:
            less_reference.append(value)
        else:
            equal_greference.append(value)

    npartition.append(less_reference)
    npartition.append(equal_greference)

    return npartition


if __name__ == "__main__":
    run([4, 3, 2, 9, 8, 5], 4)
