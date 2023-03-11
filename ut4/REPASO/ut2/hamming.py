def hamming (str1: str, str2: str)-> int:
    count = sum([ 1 for value1,value2 in zip(str1,str2) if value1 != value2])
    return count

