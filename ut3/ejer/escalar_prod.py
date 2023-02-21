v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]
result = 0
buffer = []

for num1, num2 in zip(v1, v2):
    result += num1 * num2
    op = f"{num1}·{num2}"
    buffer.append(op)

operations = " + ".join(buffer)
print(f"{operations} = {result}")
