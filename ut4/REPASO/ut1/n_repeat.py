# *************
# SUMA REPETIDA
# *************


def run(n: int, repeat: int = 3) -> int:
    if repeat == 0: 
        return 0
    result = int(str(n)*repeat) + run(n,repeat-1)
    return result

if __name__ == '__main__':
    run(2,3)
