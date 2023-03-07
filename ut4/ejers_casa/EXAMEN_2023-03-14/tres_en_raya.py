n_tablero = lambda n: {position: None for position in range(n**2)}
n = 3
tablero = n_tablero(n)
players = {"J1": "X", "J2": "O"}

def write_token (symbol: str, board: dict, position: int)-> dict:
    if board[position] is not None: 
        print("Esa posición ya está codida")
    else: 
        board[position] = symbol
change = True

while True:
    if change:
        position = int(input("Introduzca una posición: "))
        write_token(players["J1"],tablero,position)
        change = False
    else:  
        position = int(input("Introduzca una posición: "))
        write_token(players["J2"],tablero,position)
        change = True
  


