# *******************************
# VENTAS EN TIENDA DE INFORM�TICA
# *******************************


def run(sales: list) -> tuple:
    # TU C�DIGO AQU�
    pcs = displays = 0
    for sale in sales: 
        pcs += sale[0]
        displays += sale[1]
    return pcs, displays


if __name__ == '__main__':
    run([[4, 5], [1, 3], [3, 2]])