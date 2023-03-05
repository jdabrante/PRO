def r_stock(operation: list, products: dict) -> dict:
    product_code = operation[1]
    amount_replied = int(operation[2])
    if product_code in products:
        product = products[product_code]
        product["stock"] += amount_replied
    else: 
        stock_price = {"stock": 0,"price": 0}
        stock_price["stock"] = amount_replied
        products[product_code] = stock_price
    return products
