value = int(input("Introduce un valor: "))
product = 1
for i in range(1,value + 1):
    product *= i
    if i + 1 == value + 1: 
        print(f'{i}^2 = {product}', end="")
    else: 
        print(f'{i}^2 · ', end="")