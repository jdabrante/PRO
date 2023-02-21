# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    new_imoves = imoves.split(",")
    for item in new_imoves:
        key = item[0]
        value = int(item[1:])
        inventory[key] = inventory.get(key,0) + value
    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')