# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    # TU CÓDIGO AQUÍ
    # cconst = "output"
    # VOWELS = "aeiou"
    # SPACE = " "
    # set1 = set()
    # set2 = set()
    # for const in text1:
    #     if const.lower() not in VOWELS and const != SPACE:
    #         set1.add(const)
    # for const in text2:
    #     if const.lower() not in VOWELS and const != SPACE:
    #         set2.add(const)

    # repeat_const = set1 & set2
    # convert_set = sorted(list(repeat_const))
    # cconst = "".join(convert_set)

    cconst = "output"
    VOWELS = "aeiou"
    text1 = text1.replace(" ", "")
    text2 = text2.replace(" ", "")

    set1 = {const for const in text1 if const.lower() not in VOWELS}
    set2 = {const for const in text2 if const.lower() not in VOWELS}
    repeat_const = set1 & set2
    convert_set = sorted(list(repeat_const))
    cconst = "".join(convert_set)

    return cconst


if __name__ == "__main__":
    run("Flat is better than nested", "Readability counts")
