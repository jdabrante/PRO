date = "12/31/20"

date_without_bars = date.split("/")

new_date = []


if int(date_without_bars[2]) > 12:
    new_date.append(date_without_bars[1])
    new_date.append(date_without_bars[0])
    new_date.append(date_without_bars[2])
else:
    new_date = date_without_bars

# Temrinar de hacer
