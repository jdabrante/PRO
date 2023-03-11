# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    pillar_distance = gap_pillars*(num_pillars-1)*100
    total_pillar_width = num_pillars*pillar_width - (2*pillar_width)
    inter_distance = pillar_distance + total_pillar_width
    return inter_distance
if __name__ == '__main__':
    run(10, 5, 30)