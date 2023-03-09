# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(items: list, sum=0):
    if len(items) == 0:
        return sum
    if isinstance(items[0], int):
        sum += items[0]
        if len(items) == 1:
            return sum
    else:
        return sum_nested(items[1:], sum)
