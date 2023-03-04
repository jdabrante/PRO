# *****************
# N�MEROS PERFECTOS
# *****************
def proper_div (number: int)-> list:
    proper_values = [ value for value in range(1,(number//2)+1) if number%value == 0]
    proper_values = sum(proper_values)
    return proper_values

def is_perfect(number: int):
    total_proper_value = proper_div(number)
    if total_proper_value == number:
        return True
    else: 
        return False

