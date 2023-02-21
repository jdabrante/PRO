name = input("Dame tu nombre: ")

while not name.istitle():
    name = input("Dame tu nombre: ")
    print(f"{name} debe escribrirlo correctamente")


# While True:
#    name = input("Nombre: ")
#    if name.istitle():
#        print(name)
#        break
#   print("Error en el nombre")

# While not (name := input("Nombre: ")).istitle():
#   print("Error")
