value = input("Introduce un valor: ")
repetition = int(input("Introduce el numero de veces que quieres que se multiple: "))

for i in range(1,repetition):
    number = value*i
    total = int(number) * int(number)
    print(f'{" "*(repetition-i)}{number} · {number} = {total}')
