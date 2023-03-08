# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text: str, index=0, count=0):
    VOWELS = "aeiou"
    if text[index] in VOWELS:
        count += 1
    if index == len(text) - 1:
        return count
    index += 1
    return count_vowels(text, index, count)
