def order(operation: list,money: int, products: dict) -> tuple:
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

