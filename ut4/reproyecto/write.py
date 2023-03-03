def write2(path: Path, products: dict, money: int):
    output = []
    with open(path,"w") as f:
        f.write(f'{money}\n')
        products = dict(sorted([[key,value] for key,value in products.items()]))
        for code, detailes in products.items():
            output.append(code)
            for value in detailes.values():
                output.append(str(value))
            f.write(f'{" ".join(output)}\n')
            output = []
