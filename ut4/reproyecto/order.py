from stock_price import price_rest
from money import rest_money
operations=[["R","D12","7"],["R","A9","8"],["P","D12","2"],["R","B9","20"],["R","A9","8"],["P","A9","5"],["M","20"]]
products = {}
money = 0
for operation in operations:
    match operation[0]:
        case "R":
            price_rest(operation,products)
        case "P":
            price_rest(operation,products)
        case "M":
            money = rest_money(operation,money)

money 
products

operation=["O","D12","4","14"]

def order(operation: list,money: int) -> tuple:
    product_code = operation[1]
    required_amount = int(operation[2])
    money_given = int(operation[3])
    if product_code in products:
        product = products[product_code]
        stock, price = product.values()
        if (price*required_amount <= money_given) and (stock >= required_amount):
            exchange = money_given - price*required_amount
            money += money_given - exchange 
            product["stock"] -= required_amount
            products[product_code] = product
    return money

money = order(operation,money)
money 
products
    