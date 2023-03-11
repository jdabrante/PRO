# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************

def consecutive_seq(items, target_count, count=1):
    if len(items) == 1:
        return False
    if items[0] == items[1]:
        count += 1
        if count == target_count:
            return items[0]
    return consecutive_seq(items[1:],target_count,count)
