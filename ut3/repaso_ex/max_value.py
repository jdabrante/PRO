# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    # Se toma el índice 0 para comparar, ya que el primer valor que se compara consigo mismo nunca va a ser menor que él mismo.
    max_value = values[0]
    for value in values:
        if max_value < value:
            max_value = value
    return max_value


if __name__ == "__main__":
    run([-11, 10, -6, 15, -1])
