# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

#     Only lower case letters will be used (a-z). No punctuation or digits will be included.
#     Performance needs to be considered.

# Examples

# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# def scramble(s1,s2):
def scramble(s1,s2):
    char_dicc = lambda s: {char: s.count(char) for char in s}
    s1_dict = char_dicc(s1)
    s2_dict = char_dicc(s2)
    for char,amount in s2_dict.items():
        if s1_dict[char] < amount:
            result = False
            break
        else: 
            result =  True

    return result


# def scramble(s1,s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True