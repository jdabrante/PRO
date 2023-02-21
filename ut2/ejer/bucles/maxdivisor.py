a = 12
b = 44
product = 1


"""while True:
    if a % 2 == 0 and b % 2 == 0:
        product *= 2
        a /= 2
        b /= 2
    else:
        if a % 3 == 0 and b % 3 == 0:
            product *= 3
            a /= 3
            b /= 3
        else:
            if a % 5 == 0 and b % 5 == 0:
                product *= 5
                a /= 5
                b /= 5

            else:
                if a % 5 == 0 and b % 5 == 0:
                    product *= 7
                    a /= 7
                    b /= 7
                else:
                    break
print(product)"""

_min = a if a < b else b
for num in range(_min, 0, -1):
    if a % num == 0 and b % num == 0:
        break
print(num)
