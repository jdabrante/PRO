name = input("Introduce tu nombre: ")
while not name.istitle():
    print("Error. Debe escribirlo correctamente")
    name = input("Vuelva a intentarlo: ")