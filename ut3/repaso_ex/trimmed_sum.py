# **************
# SUMA RECORTADA
# **************


# def run(values: list) -> int:
#     tsum = 0
#     values.sort()
#     new_values = []

#     for value in values:
#         if value not in new_values:
#             new_values.append(value)

#     if (new_values != []) and (len(new_values)) > 1:

#         del new_values[len(new_values) - 1]
#         del new_values[0]
#         tsum = sum(new_values)

#     return tsum


def run(values: list) -> int:
    values.sort()
    new_list = []
    for value in values:
        if value not in new_list:
            new_list.append(value)
    tsum = sum(new_list[1 : len(new_list) - 1])

    return tsum


if __name__ == "__main__":
    run([6, 2, 1, 8, 10])
