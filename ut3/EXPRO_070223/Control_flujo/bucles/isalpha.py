ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
text = input("Introduzca una palabra: ")

for char in text: 
    if char not in ALPHABET: 
        result = "Se han encontrado caracteres no alfabéticos"
    else: 
        result = "Todos los caracteres son alfabéticos"
print(result)