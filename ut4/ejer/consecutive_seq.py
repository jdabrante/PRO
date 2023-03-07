# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(items, target_count):
    algo = set(items[: target_count - 1])
    if len(algo) == 1 and items[0] in algo:
        return items[0]
    elif len(items) == target_count + 1:
        return False
    else:
        return consecutive_seq(items[target_count:], target_count)
