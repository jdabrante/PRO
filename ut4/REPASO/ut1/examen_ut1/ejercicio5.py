replace_dict = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"," ":"-"}

def slug(text: str, replace_dict: dict)-> str: 
    for char in text: 
        if char in list(replace_dict.keys()):
            text = text.replace(char,replace_dict[char])
        if char.isupper():
            text = text.replace(char,char.lower())
    return text

print(slug('Hola probando',replace_dict))
