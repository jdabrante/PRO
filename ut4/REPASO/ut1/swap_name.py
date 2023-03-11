# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    name = fullname[:fullname.find(" ")]
    surname = fullname[fullname.find(" ")+1:len(fullname)]
    swapname = f'{surname} {name}'
    return swapname


if __name__ == '__main__':
    run('John McClane')