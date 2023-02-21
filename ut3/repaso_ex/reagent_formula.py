# ************
# ELLA QUÍMICA
# ************


# def run(formula: list) -> bool:
#     one_two = (
#         ((1 in formula) and (2 not in formula))
#         or ((1 not in formula) and (2 in formula))
#         or (((1 not in formula) and (2 not in formula)))
#     )
#     three_four = (
#         ((3 in formula) and (4 not in formula))
#         or ((3 not in formula) and (4 in formula))
#         or ((3 not in formula) and (4 not in formula))
#     )
#     five_six = ((5 in formula) and (6 in formula)) or (
#         (5 not in formula) and (6 not in formula)
#     )
#     seven_eight = (7 in formula) or (8 in formula)

#     valid = all([one_two, three_four, five_six, seven_eight])

#     return valid


# if __name__ == "__main__":
#     run([7, 1, 2, 3])

# Método alejandro


def run(formula: list) -> bool:

    size_formula = len(formula)
    valid = True
    if 1 and 2 in formula:
        valid = False
    if 5 in formula and not 6 in formula:
        valid = False
    if 6 in formula and not 5 in formula:
        valid = False
    return valid


if __name__ == "__main__":
    run([7, 1, 2, 3])
