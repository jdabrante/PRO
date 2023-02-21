# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    # TU C�DIGO AQU�
    inter_distance = num_pillars*(gap_pillars*100)*pillar_width

    return inter_distance


if __name__ == '__main__':
    run(10, 5, 30)