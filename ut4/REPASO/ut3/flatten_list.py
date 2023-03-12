# ***************
# APLANA LA LISTA
# ***************

def run(elements: list, flatten: list = None) -> list:
    if flatten == None:
        flatten = []
    if len(elements) == 0:
        return flatten
    if isinstance(elements[0],list):
        run(elements[0],flatten)
        return run(elements[1:],flatten)
    else: 
        flatten.append(elements[0])
        return run(elements[1:],flatten)

elements = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

run(elements)
 

if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])