# **************************
# AQU� TIENE SU VUELTA (MAX)
# **************************


def d_reverse(d: dict) -> dict:
    unsorted_tuple_list = [(key, value) for key, value in d.items()]
    sorted_dict = dict(sorted(unsorted_tuple_list, reverse=True))
    return sorted_dict


def run(to_give_back: float, available_currencies: dict) -> dict:
    order_available_currencies = d_reverse(available_currencies)
    money_back = {}
    for money, amount in order_available_currencies.items():
        given_money = to_give_back // money
        if given_money != 0:
            money_back[money] = min(given_money, amount)
            to_give_back -= money_back[money] * money
    if to_give_back == 0:
        return money_back
    return None


if __name__ == "__main__":
    run(20, {5: 3, 2: 7, 1: 3})
