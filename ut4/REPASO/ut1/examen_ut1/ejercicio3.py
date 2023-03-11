


def change_vowels (target_vowel: str, target_offset: int, input_text: str) -> str:
    VOWELS = "aeiou"
    replace_vowel = VOWELS.find(target_vowel) + target_offset
    output_text = input_text.replace(target_vowel,VOWELS[replace_vowel])
    return output_text

print(change_vowels('a', 4, 'anatolia'))


