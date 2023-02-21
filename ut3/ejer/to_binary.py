number = 211
binary = []

while number >= 1:
    binary.append(number % 2)
    number //= 2


binary = [str(v) for v in binary[::-1]]
binary = "".join(binary)
print(binary)
