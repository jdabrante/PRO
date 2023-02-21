# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = 'data/sum_matrix/result.dat'
    matrix1_list = [] 
    matrix2_list = []
    with open(matrix1_path) as f:
        for line in f:
            line = line.strip().split()
            line_break = len(line)
            line_list = ([int(value) for value in line])
            matrix1_list.extend(line_list)
        
    with open(matrix2_path) as f:
        for line in f:
            line = line.strip().split()
            line_list = ([int(value) for value in line])
            matrix2_list.extend(line_list)
            
    with open(result_path,"w") as f: 
        index = 0
        for value1,value2 in zip(matrix1_list,matrix2_list):
            result = value1 + value2
            f.write(f'{result}')
            index += 1
            if index%line_break == 0:
                f.write("\n")
            else:
                f.write(" ") 
        


    return filecmp.cmp(result_path, 'data/sum_matrix/.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')