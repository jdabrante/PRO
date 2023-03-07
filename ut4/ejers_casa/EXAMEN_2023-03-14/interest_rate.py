# *****************
# INTER�S COMPUESTO
# *****************
calc = lambda a,r,y: a * (1 + r/100)**y 

def run(amount: float, rate: float, years: int) -> float:
    return calc(amount,rate,years)
if __name__ == '__main__':
    run(10000, 3.5, 7)