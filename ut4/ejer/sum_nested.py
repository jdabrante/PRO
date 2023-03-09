# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(items: list, suma=0):
    if len(items) == 0:
        return suma 
    if isinstance(items[0], int):
        suma += items[0]
        return sum_nested(items[1:], suma)
    else: 
        for item in items[0]:
            items.append(item)
        del items[0]
        return sum_nested(items, suma)

