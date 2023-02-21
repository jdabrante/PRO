# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    # TU CÓDIGO AQUÍ
    line = None
    with open(input_path) as f:
        for i,lines in enumerate(f):
            lines = lines.strip()
            if (i + 1) == line_no:
                line = lines
        
    return line


if __name__ == '__main__':
    run('data/get_line/nasdaq.txt', 20)