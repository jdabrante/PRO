target_value = int(input("Introduce un valor: "))
value = int(input("Introduce el múltiplo: " ))
start = 0
total = 0
while total <= target_value:
    print(start)
    start += value
    total += start
    