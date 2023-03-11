def product (value: int)-> int:
    if value == 0:
        return 1
    result = value**2 * product(value - 1)
    return result

