# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    # TU CÓDIGO AQUÍ
    _freq_1 = {}
    with open(input_path) as f: 
        full_file = f.read()
        full_file = full_file.replace("\n", " ").lower()
        full_file_list = full_file.split()
        for word in full_file_list:
            if word not in _freq_1:
                _freq_1[word] = 1
            else: 
                _freq_1[word] += 1
        freq = _freq_1.copy()
        for key,value in _freq_1.items():
            if value < lower_bound:
                del freq[key]
                
                
                
        
                    

    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)