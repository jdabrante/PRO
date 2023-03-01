# ********************
# AQU� TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_money_currencies: list) -> dict:
    money_currencies = sorted(available_money_currencies, reverse=True)
    money_back = {}
    if to_give_back:
        for available_money in money_currencies:
            money_back[available_money] = to_give_back // available_money
            to_give_back = to_give_back % available_money
            if to_give_back == 0:
                return money_back
    else:
        return money_back


if __name__ == "__main__":
    run(20, [5, 2, 1])
