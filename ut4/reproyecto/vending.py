# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

def read2 (path: str)-> list: 
    with open(path) as f:
        operations = [ line.strip().split() for line in f]
    return operations

def rest_money (operation: list, vending: dict) -> dict:
    vending["money"] += int(operation[1])
    return vending

def write2(path: Path, vending: dict):
    output = []
    with open(path,"w") as f:
        money = vending["money"]
        products = vending["products"]
        f.write(f'{money}\n')
        for code, detailes in sorted(products.items()):
            output.append(code)
            for value in detailes.values():
                output.append(str(value))
            f.write(f'{" ".join(output)}\n')
            output = []

def r_price(operation: list, vending: dict) -> dict:
    product_code = operation[1]
    value_change = int(operation[2])
    products = vending["products"]
    if product_code in products:
        product = products[product_code]
        product["price"] = value_change
    return vending

def r_stock(operation: list, vending: dict) -> dict:
    product_code = operation[1]
    amount_replied = int(operation[2])
    products = vending["products"]
    if product_code in products:
        product = products[product_code]
        product["stock"] += amount_replied
    else: 
        stock_price = {"stock": amount_replied,"price": 0}
        products[product_code] = stock_price
    return products

def order(operation: list,vending: dict) -> tuple:
    product_code = operation[1]
    required_amount = int(operation[2])
    money_given = int(operation[3])
    products = vending["products"]
    if product_code in products:
        product = products[product_code]
        stock, price = product.values()
        if (price*required_amount <= money_given) and (stock >= required_amount):
            vending["money"] += price*required_amount
            product["stock"] -= required_amount
            products[product_code] = product
    return vending

def run(operations_path: Path) -> bool:
    status_path = 'data/vending/status.dat'
    vending = {"money":0,"products":{}}
    operations = read2(operations_path)

    for operation in operations:
        match operation[0]:
            case "O":
                order(operation,vending)
            case "R":
                r_stock(operation, vending)
            case "P":
                r_price(operation, vending)
            case "M":
                rest_money(operation, vending)
                
    write2(status_path, vending)

    return filecmp.cmp(status_path, 'data/vending/.expected', shallow=False)

if __name__ == '__main__':
    run('data/vending/operations.dat')