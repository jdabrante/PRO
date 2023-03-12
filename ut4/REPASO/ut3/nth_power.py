# *************
# N ELEVADO A N
# *************


def run(values: list, power: int) -> int:
    if power >= len(values):
        return -1
    return values[power]**power
if __name__ == '__main__':
    run([1, 2, 3, 4], 2)

# def len_list (values: list):
#     def calculator (power):
#         if power >= len(values):
#             return -1
#         return values[power]**power
#     return calculator

# lista1 = len_list([1, 2, 3])
# result = lista1(3)
# print(result)