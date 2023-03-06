# *****************
# ALFABETO CIRCULAR
# *****************

def aux_letter (lim):
    LETTERS = "abcdefghijklmnopqrstuvwxyz"
    abc_len = len(LETTERS)
    while lim > 0:
        choose = min(abc_len, lim)
        for i in range(choose):
            yield LETTERS[i]
        lim -= abc_len

def run(max_letters: int) -> str:
    text = "".join([ letter for letter in aux_letter(max_letters)])
    return text
if __name__ == '__main__':
    run(0)



    