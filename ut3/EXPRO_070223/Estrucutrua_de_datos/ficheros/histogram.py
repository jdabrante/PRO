# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    letters = {}
    with open(data_path) as f:
        full_file = f.read()
        copy_full_file = full_file
        copy_full_file = sorted(set(copy_full_file))
        for letter in copy_full_file:
            letters[letter] = full_file.count(letter)
    
    with open(histogram_path,"w") as f:
        for key,value in letters.items():
            f.write(f'{key} {"█"*value} {value}\n')
    return filecmp.cmp(histogram_path, 'data/histogram/.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')