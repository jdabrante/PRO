value = int(input("Introduce un número"))
matrix = ""

for i in range(value):
    for j in range(value):
        if i==j:
            matrix += " X"
        elif i>j: 
            matrix += " D"
        else: 
            matrix += " U"
    matrix += "\n"

print(matrix)