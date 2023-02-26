VENDING_PATH = 'ut4/te1/data/vending.dat'
OPERATION_PATH = 'ut4/te1/data/operations.dat'

with open(VENDING_PATH, encoding="utf8") as f1, open(OPERATION_PATH, encoding="utf8") as f2:
    coins = f1.readline().split()
    two_coin = coins[0]
    one_coin = coins[1]
    fifty_coin = coins[2]
    vending_dict={}
    operation_list = []
    for line in f1:
        line = line.strip().split()
        vending_dict[line[0]]=line[1:]
    
    for line in f2:
        line = line.strip().split()
        operation_list.append(line)

    print(operation_list)
    print(vending_dict)
        
        
        
        

    
    # def order(product,amount,first_coin,second_coin,third_coin):
        
        
    
    
    for operation in operation_list:
        if operation == 'O':
            print('Hola')
        elif operation == 'R':
            print('Its Restock')
        elif operation == 'P':
            print('Its Price')
       
status_path = 'ut4/te1/data/status.dat'     
with open(status_path, 'w', encoding="utf8") as f3:
    f3.write(f'Hola')


