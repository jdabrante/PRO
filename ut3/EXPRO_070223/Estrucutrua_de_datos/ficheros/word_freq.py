# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    freq = {}
    full_file = ""
    with open(input_path) as f:
        for line in f:
            line = line.strip().lower()
            full_file += f'{line} '
        full_file = full_file.split()
        for word in full_file:
            if full_file.count(word) >= lower_bound:
                freq[word] = full_file.count(word)
           
    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)