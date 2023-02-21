# ***************
# TUPLA DE DUPLAS
# ***************


def run(input: tuple) -> set:
    # TU CÓDIGO AQUÍ
    first_output = set()
    second_output = set()
    output = (first_output, second_output)
    for first, second in input:
        first_output.add(first)
        second_output.add(second)
    return output


if __name__ == "__main__":
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))

# Al ser datos mutables no se pueden hacer lo siguiente:

# first_ouput = second_output = set().
