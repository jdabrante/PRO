# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    # TU C�DIGO AQU�
    winner = 'output'
    for player in points: 
        winner = player
    return winner


if __name__ == '__main__':
    run('ABAABA')