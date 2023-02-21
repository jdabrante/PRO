# value_list = [1, 1, 1, 1, 1, 1, 1]

# if value_list.count(value_list[0]) == len(value_list):
#     answer = "Igual"
# else:
#     answer = "Desigual"
# print(answer)

# -----------------------------------

value_list = [1, 1, 1, 1, 1, 1, 1]

avg = sum(value_list) / len(value_list)

for value in value_list:
    if value != avg:
        print("No son iguales")
        break
else:
    print("Son iguales")
