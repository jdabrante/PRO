# ***********
# �HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    # TU C�DIGO AQU�
    available = True if stock.get(merch, 0) >= amount else False
    return available


if __name__ == '__main__':
    run({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9)