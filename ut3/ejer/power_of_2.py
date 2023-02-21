# base = 2
# number = 4
# exponent = range(number + 1))

# result = []

# for i in exponent:
#     result.append(base**i)
# print(result)

base = 2
number = 4

result = [base**i for i in range(number + 1)]

print(result)
