# La función que calculo por último, se tiene que comparar con la anterior. Se tiene que comparar el value1 que es el último con el value2 que es el reciente
n = 9
y = 0
last_y = 0



for x in range(n, -n -1, -1):
    if last_y <= y:
        last_y = y
        y = (x**2) - (6*x) + 3
        print(x)
        print(last_y)


