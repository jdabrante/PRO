# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'
    line_list = []
    with open(text_path) as f: 
        for line in f:
            num_tabs = line.count("\t")
            line = line.strip("\t")
            line_list.append(f'{"#"*num_tabs}# {line}')
            
    with open(md_path,"w") as f:
        for line in line_list:
            f.write(line)

    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')