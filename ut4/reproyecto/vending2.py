from money import rest_money
from order import order
from read import read2
from stock_price import price_rest
from write import write2

money = 0
products = {}
operations = read2("operations.dat")

for operation in operations:
    match operation[0]:
        case "O":
            money = order(operation, money, products)
        case "R":
            price_rest(operation, products)
        case "P":
            price_rest(operation, products)
        case "M":
            money = rest_money(operation, money)
            
write2(products, money)

