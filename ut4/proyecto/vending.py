VENDING_PATH = 'data/vending.dat'
OPERATION_PATH = 'data/operations.dat'
products_dict={}
operations_list = []


with open(VENDING_PATH, encoding="utf8") as f1, open(OPERATION_PATH, encoding="utf8") as f2:
    coins = f1.readline().split()
    coins = [int(coin) for coin in coins]

    for line in f1:
        line = line.strip().split()
        products_dict[line[0]]=line[1:]
    
    for line in f2:
        line = line.strip().split()
        operations_list.append(line)

def order(operation,coins,products_dict):
    if operation[1] in products_dict and operation[2] <= (products_dict[operation[1]][0]):
        order_total_coins = [int(coin_amount) for coin_amount in operation[3:]]
        calc_price = [int(operation[3]) * 2, int(operation[4]), int(operation[5])* 0.50]
        product = operation[1]
        requested_amount = operation[2]
        stock,value = products_dict[product]
        # Esto seria una función    
        coins = [value1 + value2 for value1, value2 in zip(order_total_coins,coins)]
        # Devolución de dinero
        total_paid = sum(calc_price)
        total_price = float(value) * int(requested_amount)
        if total_paid >= total_price:
            change = total_paid - total_price
            types_of_coins = [2,1,0.50]
            list_change = []
            for coin in types_of_coins: 
                if change % coin == 0: 
                    requested_amount = change/coin
                    change -= requested_amount*coin
                    list_change.append(int(requested_amount))
                else: 
                    list_change.append(0)
            coins = [value1 - value2 for value1,value2 in zip(coins,list_change)]
            products_dict[product][0] = int(stock) - int(requested_amount)
    return coins,products_dict

               
    

for operation in operations_list:
    match operation[0]:
        case "O":
            print(order(operation,coins,products_dict))
            
            
            
            
            # if operation[1] in products_dic and operation[2] <= products_dict[operation[1]][0]
            #     order_total_coins = [int(coin_amount) for coin_amount in operation[3:]]
            #     calc_price = [int(operation[3]) * 2, int(operation[4]), int(operation[5])* 0.50]
            #     product = operation[1]
            #     requested_amount = operation[2]
            #     stock,value = products_dict[product]
            #     # Esto seria una función
                
            #     coins = [value1 + value2 for value1, value2 in zip(order_total_coins,coins)]
                
            #     # Devolución de dinero
                
            #     total_paid = sum(calc_price)
            #     total_price = float(value) * int(requested_amount)
            #     if total_paid >= total_price:
            #         change = total_paid - total_price
            #         types_of_coins = [2,1,0.50]
            #         list_change = []
            #         for coin in types_of_coins: 
            #             if change % coin == 0: 
            #                 requested_amount = change/coin
            #                 change -= requested_amount*coin
            #                 list_change.append(int(requested_amount))
            #             else: 
            #                 list_change.append(0)
            #         coins = [value1 - value2 for value1,value2 in zip(coins,list_change)]
            #         products_dict[product][0] = int(stock) - int(requested_amount)
                    
                    
                

                
                
        # case "R":
        #     print ("Se repone")
        # case "P":
        #     print ("Se cambia el precio")
        # case "C":
        #     print ("Se introduce dinero")
                
    
# products_dict = [" ".join([key," ".join(value)]) for key,value in products_dict.items() ]
        
# print(products_dict)
    
#     # def order(product,amount,first_coin,second_coin,third_coin):
        
        
# status_path = 'data/status.dat'     
# with open(status_path, 'w', encoding="utf8") as f3:
#     coins = [str(coin) for coin in coins]
#     f3.write(f'{" ".join(coins)}\n')
#     for status in products_dict:
#         f3.write(f'{status}\n')
    


