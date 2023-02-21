# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = "data/common_words/output.txt"
    # TU CÓDIGO AQUÍ
    with open(input_path) as f:
        lines_list = []
        repeat_list = []
        for line in f:
            stripped_line = set(line.lower().strip().split())
            lines_list.append(stripped_line)
        for set1 in lines_list:
            for set2 in lines_list:
                repeat_list.append(str(len(set1 & set2)))

    with open(output_path, "w") as f:
        repeat_words = " ".join(repeat_list)
        repeat_words = repeat_words.split()
        for word in repeat_words:
            f.write(f"{word}\n")

    return filecmp.cmp(output_path, "data/common_words/.expected", shallow=False)


if __name__ == "__main__":
    run("data/common_words/minizen.txt")
