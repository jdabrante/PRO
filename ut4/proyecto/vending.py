with open("files/vending.dat") as f: 
    money = f.readline().strip().split()
    money = [int(value) for value in money]

def final_dat(money: list): 
    with open("files/final.dat", "w") as f:
        f.write(" ".join([str(value) for value in money]))

def data():
    with open("files/final.dat") as f: 
        money = f.readline().strip().split()
        return [int(value) for value in money]
    

uno = 5
dos = 2
tres = 1





