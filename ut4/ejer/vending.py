# stock
# articulo
# precios
# pedido
# dinero
def vending(order, cash):
    # Tiene que ir en un fichero, aquí no tiene sentido
    articles = {"Coca-cola": {2: 10}, "Chocolate": {2: 12}, "Millo": {1: 15}}
    result = "No existe el producto"
    if articles[order]:
        for price, stock in articles[order].items():
            if stock >= 0 and price <= cash:
                result = [order, abs(price - cash)]
                stock -= 1
                articles[order].update({price: stock})
    return result


resultado = vending("Chocolate", 3)
resultado
