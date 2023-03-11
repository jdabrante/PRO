first_move = lambda p,r: p + 1 + r
second_move = lambda p,r: p + 2 - r

def knight (x_target: int, y_target: int, x: int = 0, y: int = 0):
    r = True
    while x != x_target and y != y_target:
        x = first_move(x,r)
        y = second_move(y,r) 
        if r == True:
            r = False
        else:
            r = True
        yield x,y

print(list(knight(8,7)))