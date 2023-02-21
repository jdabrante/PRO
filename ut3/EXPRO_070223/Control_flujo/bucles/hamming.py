num1 = "0001010011101"
num2 = "0000110010001"
hamming = 0
for i in range(len(num1)):
    if num1[i] != num2[i]:
        hamming += 1
print(hamming)