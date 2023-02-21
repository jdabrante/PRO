# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    with open(input_path) as f: 
        months_temp_avg = []
        for line in f: 
            temps_months = line.strip().split(",")
            temps_num_values = len(temps_months)
            temp_values_month = [int(value) for value in temps_months] 
            total_temps_months = sum(temp_values_month)
            avg_temps_months = total_temps_months/temps_num_values
            months_temp_avg.append(avg_temps_months)
        
        with open(output_path, "w") as f:
            for value in months_temp_avg:
                real_value = value
                f.write(f'{real_value:.2f}\n')

    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')