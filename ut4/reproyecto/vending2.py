# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

def read2 (path: str)-> list: 
    with open(path) as f:
        operations = [ line.strip().split() for line in f]
    return operations

def rest_money (operation: list, money: int) -> int:
    money += int(operation[1])
    return money

def write2(path: Path, products: dict, money: int):
    output = []
    with open(path,"w") as f:
        f.write(f'{money}\n')
        for code, detailes in sorted(products.items()):
            output.append(code)
            for value in detailes.values():
                output.append(str(value))
            f.write(f'{" ".join(output)}\n')
            output = []
            
def r_price(operation: list, products: dict) -> dict:
    product_code = operation[1]
    target_feature = int(operation[2])
    if product_code in products:
        product = products[product_code]
        product["price"] = target_feature
    return products

def r_stock(operation: list, products: dict) -> dict:
    product_code = operation[1]
    amount_replied = int(operation[2])
    if product_code in products:
        product = products[product_code]
        product["stock"] += amount_replied
    else: 
        stock_price = {"stock": amount_replied,"price": 0}
        products[product_code] = stock_price
    return products

def order(operation: list,money: int, products: dict) -> tuple:
    product_code = operation[1]
    required_amount = int(operation[2])
    money_given = int(operation[3])
    if product_code in products:
        product = products[product_code]
        stock, price = product.values()
        if (price*required_amount <= money_given) and (stock >= required_amount):
            money += price*required_amount
            product["stock"] -= required_amount
            products[product_code] = product
    return money

def run(operations_path: Path) -> bool:
    status_path = 'data/vending/status.dat'
    money = 0
    products = {}
    operations = read2(operations_path)

    for operation in operations:
        match operation[0]:
            case "O":
                money = order(operation, money, products)
            case "R":
                r_stock(operation, products)
            case "P":
                r_price(operation, products)
            case "M":
                money = rest_money(operation, money)
                
    write2(status_path, products, money)

    return filecmp.cmp(status_path, 'data/vending/.expected', shallow=False)

if __name__ == '__main__':
    run('data/vending/operations.dat')