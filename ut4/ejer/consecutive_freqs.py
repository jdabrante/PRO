# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************

def cfreq(items, /, as_string=False):
    freqs = []
    if len(items) > 0: 
        count = 0
        last_number = items[0]

        for number in items:
            if last_number == number:
                count += 1
            else: 
                freqs.append((last_number,count))
                count = 1
                last_number = number
        freqs.append((last_number,count))
    
    if as_string:
        string_values = [f'{number}:{repeat}' for number,repeat in freqs]
        freqs = ",".join(string_values)
    
    return freqs





