def cartesian_product (str1: str, str2: str)-> list:
    mix = []
    for char1 in str1:
        for char2 in str2: 
            mix.append(f'{char1}{char2}')
    return mix

print(cartesian_product("abc","123"))