
square = lambda a,b: a**2+b**2
square_root = lambda a,b: (a*b)**0.5

def operation(a: int, b: int)-> int: 
    result = square(a,b) - square_root(a,b)
    return result

