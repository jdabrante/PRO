# **********
# PAL�NDROMO
# **********


def is_palindrome(text: str)-> bool:
    text = text.lower().replace(" ","")
    rev_text = text[::-1]
    if rev_text == text: 
        palindrome_text = True
    else: 
        palindrome_text = False
    return palindrome_text





    

