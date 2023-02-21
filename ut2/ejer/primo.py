num = 11
number_multiply = 0

for i in range(
    1, (num / 2) + 1
):  # Se utiliza el num/2 debido a que un número solo podrá ser divisible hasta su mitad.
    if num % i == 0:
        number_multiply += 1

if number_multiply == 2:
    print("Es primo")
else:
    print("No es primo")
