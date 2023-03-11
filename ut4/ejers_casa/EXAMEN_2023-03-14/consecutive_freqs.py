# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************
def cfreq(elements: list, /,strng=False):
    result = []
    count = 1
    for i in range(len(elements)-1):
        current_number = elements[i]
        next_number = elements [i + 1]
        if current_number == next_number:
            count += 1
        else: 
            result.append((current_number,count))
            count = 1
    if len(elements):
        final_num = len(elements)-1
        result.append((elements[final_num],count))
    if strng == False: 
        return result
    else: 
        result = [ f'{number}:{repeat}' for number,repeat in result]
        return ",".join(result)

