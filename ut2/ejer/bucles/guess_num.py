number = None
TARGET_NUMBER = 87
attempts = 0

while number != TARGET_NUMBER:
    attempts += 1
    number = int(input("Introduce un número:"))
    if number > TARGET_NUMBER:
        print(f"{number} es mayor que el número a descubrir")
    elif number < TARGET_NUMBER:
        print(f"{number} es menor que el número a descubrir")

print(f"Es correcto. Número de intetos: {attempts}")
