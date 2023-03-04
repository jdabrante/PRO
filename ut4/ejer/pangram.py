# ********
# PANGRAMA
# ********


def is_pangram(text: str)-> bool:
    letters = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    full_text = text.lower().replace(" ","")
    for char in full_text: 
        if char not in letters: 
            letters.append(char)
    if len(abc) == len(letters):
        return True
    else: 
        return False




