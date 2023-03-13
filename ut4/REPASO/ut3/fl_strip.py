# ****************
# TROCEADO EXTREMO
# ****************


def run(numbers: str) -> str:
    strip_numbers = numbers[1:len(numbers)-1].replace(","," ").strip()
    return strip_numbers
if __name__ == '__main__':
    run('1,2,3')