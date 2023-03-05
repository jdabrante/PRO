def r_price(operation: list, products: dict) -> dict:
    product_code = operation[1]
    target_feature = int(operation[2])
    if product_code in products:
        product = products[product_code]
        product["price"] = target_feature
    return products
