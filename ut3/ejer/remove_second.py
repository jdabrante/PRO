"""
Dada una lista, genere otra lista eliminando el segundo elemento de forma repetida.
"""


# def run(items: list) -> list:
#     filter = []
#     condition = True
#     for item in items:
#         if condition == True:
#             filter.append(item)
#             condition = False
#         else:
#             condition = True
#     return filter


# -----------------------------------------


# def run(items: list) -> list:
#     filter = items[::2]
#     return filter

# -----------------------------------------


def run(items: list) -> list:
    filter = []
    for i, item in enumerate(items):
        if i % 2 == 0:
            filter.append(item)
    return filter
