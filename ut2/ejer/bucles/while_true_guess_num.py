TARGET_NUMBER = 44

# La condición que se utilizaría en el while se utiliza en el if. La ventaja de utilizar un while True es que no tienes que tener un valor antes.
while True:
    user_input = int(input("Dame un número"))
    if user_input > TARGET_NUMBER:
        print("Menor")
    if user_input < TARGET_NUMBER:
        print("Mayor")
    else:
        break
print("Correcto")
