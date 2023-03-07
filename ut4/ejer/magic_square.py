# ***************
# CUADRADO M�GICO
# ***************

total_row = lambda m: [sum(values) for values in m]

def total_column (m: list)-> list: 
    tcolumn = []
    if m:
        for i in range(len(m)):
            column = []
            for value in m:
                column.append(value[i])
            tcolumn.append(sum(column))
    return tcolumn

def total_left_di (m: list)-> int:
    di = 0
    if m:
        for i in range(len(m)):
            for j in range(len(m)):
                if i == j:
                    di += m[i][j]
    return di

def total_right_di (m: list)-> int:
    change_m = [ value[::-1] for value in m]
    di = total_left_di(change_m)
    return di
            
def is_magic_square(m):
    total = []
    total.append(total_right_di(m))
    total.append(total_left_di(m))
    for value in total_column(m):
        total.append(value)
    for value in total_row(m):
        total.append(value)

    if len(total) == total.count(total[0]):
        return True
    else: 
        return False

