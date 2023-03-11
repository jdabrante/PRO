# ********************************
# UNA M�TRICA PARA CADENA DE TEXTO
# ********************************

num_vowels = lambda t,v: sum([1 for c in t if c in v])
def run(text: str, VOWELS: str = "aeiou") -> int:
    return num_vowels(text,VOWELS)*len(text)


if __name__ == '__main__':
    run('ordenador')