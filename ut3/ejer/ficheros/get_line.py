# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    line_list = []
    with open(input_path) as f:
        for line_ in f:
            stripped_line = line_.strip()
            line_list.append([stripped_line])
        if line_list[line_no - 1] in line_list and line_no > 0:
            line = "".join(line_list[line_no - 1])
        else:
            line = None

    return line


if __name__ == "__main__":
    run("data/get_line/nasdaq.txt", 20)
