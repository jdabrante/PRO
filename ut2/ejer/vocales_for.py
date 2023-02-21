sentence = "Supercalifragilisticoespialidoso"
count_vocal = 0
VOWELS = "aeiou"


for letter in sentence:
    if letter in VOWELS:
        count_vocal += 1

print(count_vocal)

