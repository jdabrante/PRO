# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    words_list = text.split()
    chars_list = [list(word) for word in words_list]
    pig_text = []
    for chars in chars_list: 
        first_letter = chars[0]
        if first_letter.isalpha():
            first_letter = chars.pop(0)
            chars.append(f'{first_letter}ay')
        word = "".join(chars)
        pig_text.append(word)
    pig_text = " ".join(pig_text)
    return pig_text

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [f'{word[1:]}{word[:1]}ay' if word.isalpha() else word for word in lst])