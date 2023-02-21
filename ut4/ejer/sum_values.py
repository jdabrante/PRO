def _sum(*values):
    result = 0
    for arg in values:
        result += arg
    return result

total_sum = _sum(1,2,3,4,5,6,7,8,9,10)
print(total_sum)