# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    longest_word = ''
    symbols = ",.;:()"
    with open(input_path) as f:
        for line in f:
            list_words = line.split()
            for word in list_words:
                stripped_word = word.strip(symbols)
                if len(stripped_word) >= len(longest_word):
                    longest_word=stripped_word 
    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')