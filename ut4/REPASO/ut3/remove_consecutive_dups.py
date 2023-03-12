# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************

final_num = lambda r,i: r.append(i[len(i)-1])

def run(items: list) -> list:
    result = []
    for i in range(len(items)-1):
        if items[i] != items[i+1]:
            result.append(items[i])
    final_num(result,items)
    return result


if __name__ == '__main__':
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])