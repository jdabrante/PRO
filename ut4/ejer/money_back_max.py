# **************************
# AQU� TIENE SU VUELTA (MAX)
# **************************

def d_reverse(d: dict)-> dict:
    lt_us = [(key,value) for key,value in d.items()]
    d_s = dict(sorted(lt_us, reverse=True))
    return d_s

def run(to_give_back: float, available_currencies: dict) -> dict:
    order_available_currencies = d_reverse(available_currencies)
    money_back = {}
    if to_give_back: 
        for money,amount in order_available_currencies.items():
            money_back[money] = to_give_back//money 
            if money_back[money] > amount:
                money_back[money] = amount
                order_available_currencies[money] = 0
            order_available_currencies[money] = amount - money_back[money]
            to_give_back -= money_back[money] * money
            if to_give_back == 0:
                return money_back
    else: 
        return money_back


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})