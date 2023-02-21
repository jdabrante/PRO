# Dada una lista de strings, obtenga otra lista que contenga todos los caracteres de cada
# uno de los strings de la lista de entrada.


def run(texts: list) -> list:
    chars = []
    for word in texts:
        for char in word:
            chars.append(char)
    # Se podria usar chars += char, pero es más ineficiente ya que apunta a otro sitio de memoria cada vez.
    return chars


# Mejor forma:
"""def run(texts: list) -> list:
    chars = []
    for word in texts:
        chars.extend(word)
    return chars"""
