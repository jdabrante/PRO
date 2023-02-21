# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different dat types.

def find_short(s):
    words = s.split()
    l = len(words[0])
    for word in words:
        if len(word) < l:
            l = len(word)
    return l

# def find_short(s):
#     return min([len(x) for x in s.split()])