# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    output_path = 'data/replace_chars/r_noticia.txt'
    replacements = replacements.strip().split("|")
    change_lines =  []
    with open(input_path) as f:
        for line in f:
            for old,new in replacements:
                line = line.replace(old,new)
            change_lines.append(line)
    
    with open(output_path,"w") as f:
        string_line = "".join(change_lines)
        f.write(string_line)

    return filecmp.cmp(output_path, 'data/replace_chars/.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', 'áa|ée|íi|óo|úu')