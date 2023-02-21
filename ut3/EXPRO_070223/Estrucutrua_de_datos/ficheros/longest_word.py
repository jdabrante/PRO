# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    SYMBOLS = (",.;:()")
    longest_word = ""
    with open(input_path) as f:
        full_file = f.read()
        full_file = full_file.strip().split()
        for word in full_file:
            word = word.strip(SYMBOLS)
            if len(word) >= len(longest_word):
                longest_word=word
        return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')