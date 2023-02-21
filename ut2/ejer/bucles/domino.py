# Escriba un programa que muestre por pantalla todas las fichas del dominó. La ficha «en blanco» se puede representar con un 0
DOMINO_MAX = 6

for i in range(DOMINO_MAX + 1):
    for j in range(i,DOMINO_MAX + 1): #Se utiliza i como el nuevo rango de inicio
        print(f'{i}|{j}', end=" ")
    print()
