# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    output_path = "data/replace_chars/r_noticia.txt"
    replacements_list = replacements.split("|")
    index = 0

    with open(input_path) as f:
        full_file = f.read()
        for old,new in replacements_list:
            full_file = full_file.replace(old, new)

    with open(output_path, "w") as f:
        f.write(full_file)

    return filecmp.cmp(output_path, "data/replace_chars/.expected", shallow=False)


if __name__ == "__main__":
    run("data/replace_chars/noticia.txt", "áa|ée|íi|óo|úu")
