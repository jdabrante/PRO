# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    # TU CÓDIGO AQUÍ
    data = []
    with open(datafile) as f: 
        atributes = f.readline()
        atributes = atributes.strip().split(",")
        for line in f: 
            fixed_values =[]
            values = line.strip().split(",")
            for value in values: 
                if value == "True":
                    value = True
                elif value == "False":
                    value = False
                elif value.isnumeric():
                    value = int(value)
                fixed_values.append(value)
            pokemon = dict(zip(atributes,fixed_values))
            data.append(pokemon)
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')