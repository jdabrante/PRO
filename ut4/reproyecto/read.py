def read2 (path: str)-> list: 
    with open(path) as f:
        operations = [ line.strip().split() for line in f]
    return operations
    