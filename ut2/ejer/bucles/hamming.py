num1 = "0001010011101"
num2 = "0000110010001"
position = 0
count = 0

for binary1 in num1:
    if num2[position] != binary1:
        count += 1
    position += 1

print(count)

""" for binary in range(len(num1)):
        if num1[binary] != num2[binary]:
            count +=1 """
