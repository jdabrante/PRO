# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    # TU C�DIGO AQU�
    
    new_value = interval.strip("()[]").split(",")
    first_value = int(new_value[0])
    second_value = int(new_value[1])
    if interval.startswith("[") and interval.endswith("]"):
        irange = list(range(first_value,second_value+1))
    elif interval.startswith("(") and interval.endswith(")"):
        irange = list(range(first_value+1,second_value))
    elif interval.startswith("(") and interval.endswith("]"):
        irange= list(range(first_value+1,second_value+1))
    else:
        irange = list(range(first_value,second_value))
    return irange


if __name__ == '__main__':
    run('[3,10]')