def max_common_div (value1, value2):
    target = min(value1,value2)
    result = 0
    for divisor in range(target, 0, -1):
        if value1%divisor == 0 and value2%divisor == 0:
            result = divisor
            break
    return result

print(max_common_div(12,44))
