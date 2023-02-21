# **********************
# ORDENANDO CON BURBUJAS
# **********************


# def bubble():
#     # TU CÓDIGO AQUÍ


def bubble(items):
    order_items = items.copy()
    messy = True

    while messy:
        messy = False
        for i in range(len(order_items) - 1):
            if order_items[i + 1] < order_items[i]:
                order_items[i + 1], order_items[i] = order_items[i], order_items[i + 1]
                messy = True
    return order_items
