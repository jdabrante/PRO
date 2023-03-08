# ***************
# CUADRADO M�GICO
# ***************

def comprobation (values: set)-> int|bool:
    if len(values) == 1:
        value_list = list(values)
        number = value_list[0]
        return number
    elif len(values) == 0:
        return sum(values)
    return False
  
def count_rows(values: list)-> bool|int:
    rows =  set([sum(value) for value in values])
    return comprobation(rows)

def count_columns(values: list)-> bool|int:
    columns = set()
    for i in range(len(values)):
        column = 0
        for value in values: 
            column += value[i]
        columns.add(column)
    return comprobation(columns)

def count_diagonal (values: list)-> int:
    di = []
    for i in range(len(values)):
        for j in range(len(values)):
            if i is j:
                di.append(values[i][j])
    return sum(di) 

def count_reverse_diagonal (values: list)-> int:
    reverse_values = [value[::-1] for value in values]
    return count_diagonal(reverse_values)

def is_magic_square(m):
    row = count_rows(m)
    column = count_columns(m)
    right_diagonal = count_diagonal(m)
    left_diagonal = count_diagonal(m)
    if row == column and column == right_diagonal and right_diagonal == left_diagonal:
        return True
    else:
        return False




