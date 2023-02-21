n = 100
num1 = 0
print(num1)
num2 = 1
print(num2)

for i in range(98):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
