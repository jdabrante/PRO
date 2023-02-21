# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    matches = []
    num_lines = 0
    symbols=".,:;()'¡!-"
    with open(data_path) as f:
        for line in f:
                num_lines +=1
                num_columns = 0
                split_line = line.lower().split()
#El already_read es necesario para que pueda contarse bien las diferentes palabras de la línea.
                for word in split_line:
                    already_read = False
                    for letter in word:
                        num_columns += 1
                        if not word.isalpha():
                            if word.strip(symbols) == target_word.lower() and already_read==False:
                                if not word[0].isalpha():
                                    num_columns += 1 
                                found_word = (num_lines,num_columns)
                                matches.append(found_word)
                                already_read = True
                        elif word.isalpha():
                            if word==target_word and already_read==False:
                                found_word = (num_lines,num_columns)
                                matches.append(found_word)
                                already_read = True
                    num_columns += 1
                    
                
                
    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', "'Tás")