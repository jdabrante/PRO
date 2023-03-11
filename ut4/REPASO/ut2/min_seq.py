def min_seq(target: int, value: int)-> list:
    values = []
    count = 0
    while sum(values) < target:
        values.append(count)
        count += value
    return values
