def find_item(values: tuple, num: int) -> int:
    """Returns the numbers of times that a values is repeated in a tuple
    The operation is:
        1. Compare if the value is equal to the input number
        2. If the number is equal to the value then add one to the count
    :param values: tuple of values to be iterated in order to number how many times a given value is repeated
    :param num: number...
    """
    count = sum([1 for value in values if value == num])
    return count
