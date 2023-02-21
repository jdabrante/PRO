# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    with open (datafile) as f:
        data=[]
        NUMBERS="1234567890"
        index=0
        first_line=f.readline()
        charact_dict={}
        for line in f:
            charact=first_line.strip().split(",")
            charact_list = line.strip().split(",")
            for value in charact_list:
                if value[0] in NUMBERS:
                     charact_dict[charact[index]] = int(value)
                     index += 1
                elif value=="False":
                    charact_dict[charact[index]] = False
                    index += 1
                elif value=="True":
                    charact_dict[charact[index]] = True
                    index += 1
                else:
                    charact_dict[charact[index]] = value
                    index += 1
            index=0
            data.append(charact_dict)
            charact_dict={} 
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')