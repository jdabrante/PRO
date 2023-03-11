# ********
# PANGRAMA
# ********


# def is_pangram(text: str)-> bool:
#     letters = []
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     full_text = text.lower().replace(" ","")
#     for char in full_text: 
#         if char not in letters: 
#             letters.append(char)
#     if len(abc) == len(letters):
#         return True
#     else: 
#         return False


def is_pangram(text: str)-> bool:
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_len = len(abc)
    text = text.lower().replace(" ","")
    text_len = len(set(text))
    if text_len == abc_len:
        return True
    else: 
        return False

