# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words: list) -> tuple[list, list]:
    lower_words = []
    upper_words = []
    for word in words:
        if word.isupper():
            upper_words.append(word)
        elif word.islower():
            lower_words.append(word)
    return lower_words, upper_words
