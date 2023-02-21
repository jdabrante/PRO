# *******************************
# VENTAS EN TIENDA DE INFORMÁTICA
# *******************************


def run(sales: list) -> tuple:
    pcs = displays = 0
    for sale in sales:
        for i, value in enumerate(sale):
            if i == 0:
                pcs += value
            else:
                displays += value
    return pcs, displays


if __name__ == "__main__":
    run([[4, 5], [1, 3], [3, 2]])
