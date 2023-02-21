entrada =  [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# Tenemos que ir leyendo la lista y ver si el siguiente es igual. si lo es, se elimina.
index = 1
for numero in entrada: 
    if numero == entrada[index] or numero == entrada[index - 1]:
        del(entrada[index])
        index += 1
    else:
        index += 1
