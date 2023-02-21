# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = "data/avg_temps/avg_temps.dat"
    months_temp = []
    avg_months_temps = []
    with open(input_path) as input_f:
        for temps in input_f:
            list_temps = temps.strip().split(",")
            for temp in list_temps:
                months_temp.append(int(temp))
            total_months_temp = sum(months_temp)
            avg_months_temps.append(total_months_temp / len(months_temp))
            months_temp = []

    with open(output_path, "w") as output_f:
        for avg_temp in avg_months_temps:
            output_f.write(f"{avg_temp:.2f}\n")

    # TU CÓDIGO AQUÍ

    return filecmp.cmp(output_path, "data/avg_temps/.expected", shallow=False)


if __name__ == "__main__":
    run("data/avg_temps/temperatures.dat")
