# ************************************
# CALCULANDO EL FACTORIAL DE UN N�MERO
# ************************************


# def factorial(n):
#     result = 1
#     if n == 0:
#         return 1
#     if n < 0: 
#         return None
#     for number in range(1,n+1):
#         result *= number
#     return result


def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return None
    return n * factorial(n - 1)