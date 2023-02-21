# input_list = [0, 0,25,25,31, 1, 2, 3, 4, 4, 5,5, 6, 6, 6, 7, 8,8,8,8, 9, 4, 4]
# output_list = [input_list[0]]

# for number in input_list:
#     index = (len(output_list)-1)
#     if number != output_list[index]:
#         output_list.append(number)
# print(output_list)

input_list = [0, 0, 25, 25, 31, 1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 8, 9, 4, 4]
prev = None
non_consecutive = []

for current in input_list:
    if current != prev:
        non_consecutive.append(current)
        prev = current

print(non_consecutive)
