string = 'aaa'

for letter in string:
    letter = ord(letter)
    letter += letter

print(letter)
