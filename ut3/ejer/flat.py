nested_values = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flated_values = []

for value in nested_values:
    if type(value) == list:
        for subvalue in value:
            flated_values.append(subvalue)
    else:
        flated_values.append(value)
print(flated_values)

# Mejor forma:

# for value in nested_values:
#     if type(value) == list:
#         flated_values.extend(value)
#     else:
#         flated_values.append(value)
