# *******************
# N�MERO EN INTERVALO
# *******************
def interval(lower_limit,upper_limit):
    inter = [number for number in range(lower_limit,upper_limit + 1)]
    return inter

def in_range(value,lower_limit, upper_limit,/):
        interval(lower_limit,upper_limit)
        return value in interval(lower_limit,upper_limit)
    

