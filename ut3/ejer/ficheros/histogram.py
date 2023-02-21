# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = "data/histogram/histogram.txt"
    letters = []
    count_letters = {}
    with open(data_path) as f:
        for line in f:
            for letter in line:
                if letter not in letters:
                    letters.append(letter)
        letters.sort()
        for letter in letters:
            count_letters[letter] = line.count(letter)

    with open(histogram_path, "w") as f:
        for letter, value in count_letters.items():
            f.write(f'{letter} {"█" * value} {value}\n')

    return filecmp.cmp(histogram_path, "data/histogram/.expected", shallow=False)


if __name__ == "__main__":
    run("data/histogram/data.txt")
