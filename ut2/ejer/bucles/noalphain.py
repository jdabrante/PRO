sentence = "Hello-World"

for letter in sentence:
    if not letter.isalpha():
        print("Se ha encontrado caracteres no alfabeicos")
        break
else:
    print("Todos los caracteres son alfabéticos")
