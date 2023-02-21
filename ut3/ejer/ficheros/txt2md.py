# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'
    lines = []
    with open(text_path) as f:
        for line in f:
            _t_count = line.count("\t")
            line_without_t = line.strip("\t")
            line_with_hash = f'#{"#"*_t_count} {line_without_t}'
            lines.append(line_with_hash)
    with open(md_path, "w") as f:
        for line in lines:
            f.write(line)

    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')