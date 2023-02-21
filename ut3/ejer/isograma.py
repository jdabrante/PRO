word = "mnr"
letters_in_word = []

for letter in word.lower():
    if letter in letters_in_word:
        answer = "no es un siograma"
        break
    if letter.isalpha():
        letters_in_word.append(letter)
else:
    result = "es un isograma"
print(f"{word} {result}")
