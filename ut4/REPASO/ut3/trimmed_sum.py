# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    tsum = 0
    if len(values) > 0:
        target_values = [max(values),min(values)]
        tsum = sum([value for value in values if value not in target_values])
    return tsum
if __name__ == '__main__':
    run([6, 2, 1, 8, 10])