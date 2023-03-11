# ***************
# CONTANDO OVEJAS
# ***************


def run(num_sheeps: int, word: str = "sheep...") -> str:
    if num_sheeps == 0:
        return ""
    sleep = word + run(num_sheeps - 1, word)
    return sleep
if __name__ == '__main__':
    run(0)