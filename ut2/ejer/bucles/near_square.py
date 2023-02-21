number = 10
square = (number) ** (1 / 2)
count = 0


while True:
    if square % 1 != 0:
        up = (number + count) ** (1 / 2)
        down = (number - count) ** (1 / 2)
        count += 1
        if up % 1 == 0:
            answer = up
            break
        elif down % 1 == 0:
            answer = down
            break
    else:
        answer = number
        break
print(round(answer**2))
