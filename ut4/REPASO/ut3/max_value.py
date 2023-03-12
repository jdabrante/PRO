# ************
# VALOR M�XIMO
# ************

check_max = lambda a,b: True if a > b else False

def run(values: list) -> int:
    max_value = values[0]
    for value in values: 
        if check_max(value,max_value):
            max_value = value
    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])