# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    irange = ""

    new_interval = list(interval)
    all_closed = interval[0] == "[" and interval[len(interval) - 1] == "]"
    first_closed = interval[0] == "[" and interval[len(interval) - 1] == ")"
    first_open = interval[0] == "(" and interval[len(interval) - 1] == "]"
    all_open = interval[0] == "(" and interval[len(interval) - 1] == ")"

    for character in interval:
        if character != interval[0] and character != interval[len(interval) - 1]:
            irange += character
    irange = irange.split(",")

    irange_int = []

    for value in irange:
        irange_int.append(int(value))

    if all_closed:
        sum_value = 0
        irange = [irange_int[0]]
        while sum_value < irange_int[len(irange_int) - 1]:
            sum_value += 1
            irange.append(sum_value)

    # elif first_closed:
    #     irange =
    # elif first_open:
    #     irange =
    # elif all_open:
    #     irange =
    # return irange


if __name__ == "__main__":
    run("[3,10]")
