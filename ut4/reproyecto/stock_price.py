def price_rest(operation: list, products: dict) -> dict:

    operation_type = operation[0]
    product_code = operation[1]
    target_feature = int(operation[2])
    if operation_type == "R":
        target = "stock"
    else:
        target = "price"
    if product_code in products:
        product = products[product_code]
        if operation_type == "R":
            product[target] += target_feature
        else:
            product[target] = target_feature
    elif product_code not in products and operation_type == "R":
        stock_price = {"stock": 0, "price": 0}
        stock_price[target] = target_feature
        products[product_code] = stock_price
    return products
