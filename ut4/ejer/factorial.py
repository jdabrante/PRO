# ************************************
# CALCULANDO EL FACTORIAL DE UN N�MERO
# ************************************


def factorial(n):
    mult = 1
    if n >= 0:
        for number in range(n, 0, -1):
            mult *= number
    else:
        mult = None
    return mult
