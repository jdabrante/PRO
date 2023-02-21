# *************************
# ECUACI�N DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:
    # TU CÓDIGO AQUÍ
    x1 = x2 = 'output'
    discriminant = ((b**2)-4*a*c)**0.5

    x1 = (-b+discriminant)/(2*a)
    x2 = (-b-discriminant)/(2*a)


    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)