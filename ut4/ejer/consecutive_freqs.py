# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


# def cfreq(items, /, as_string=False):
#         consecutive_numbers  = []
#         consecutive_number = []
#         for item in items:
#             if item != consecutive_number[0]:
#                   consecutive_number=[]
#             if item not in consecutive_number:
#                   repeat = 1
#                   consecutive_number.append(item,repeat)
#             else:
#                   consecutive_number[1] += 1
#     return

items = [2, 2, 1, 1, 2, 2, 1, 1]

# consecutive_numbers = []
# repeat = 0
# for i,item in enumerate(items):
#     if i == 0:
#         last_number = item
#         consecutive_numbers.append(item)
#         consecutive_numbers.append(repeat)
#     if item == last_number:
#         consecutive_numbers[1] += 1
#     elif i != 0 and item != last_number:
#         consecutive_numbers.append(item)
#         consecutive_numbers.append(repeat)
def cfreq(items, /, as_string=False):
    if not items:
        if as_string:
            return ""
        else:
            return []
    consecutive_numbers = []
    consecutive_number = [None]
    for item in items:
        if item != consecutive_number[0]:
            if consecutive_number[0] == None:
                consecutive_number = []
            else:
                consecutive_numbers.append(tuple(consecutive_number))
                consecutive_number = []
        if item not in consecutive_number:
            repeat = 1
            consecutive_number.append(item)
            consecutive_number.append(repeat)
        else:
            consecutive_number[1] += 1
    consecutive_numbers.append(tuple(consecutive_number))
    if as_string:
        final_consecutive_numbers = []
        for value, repeat in consecutive_numbers:
            final_consecutive_numbers.append(f"{value}:{repeat}")
        freqs = ",".join(final_consecutive_numbers)
    else:
        freqs = consecutive_numbers
    return freqs
