# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    matches = []
    SYMBOLS = (".,:;()'!¡")
    num_line = 0
    with open(data_path) as f:
        for line in f:
            num_column = 0
            num_line += 1
            line_list = line.strip().split()
            if target_word.lower() in line.lower():
                for word in line_list:
                    already_read = False
                    for char in word:
                        target_condition = word.lower().strip(SYMBOLS) == target_word.lower() and already_read == False 
                        num_column += 1 
                        if target_condition:
                            if not char.isalpha():
                                num_column += 1
                            already_read = True
                            found_word = (num_line,num_column)  
                            matches.append(found_word)
                    num_column += 1
                
             
                        
    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'Tás')