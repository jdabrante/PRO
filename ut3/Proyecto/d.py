board = []
size = 3

# -------Se crea el tablero-------

for row in range(size):
    board.append([])
    for column in range(size):
        board[row].append(f"{row},{column}")

# -------Se inicializa las variables de juego-------


is_player1 = True
player1_symbol = " X "
player2_symbol = " 0 "
decisions = ["", ""]


# -------Juego-------


for _ in range(size * size):
    visual_board = ""

    # -------Se imprime el tablero-------

    for row in board:
        visual_board += " | ".join(row) + "\n\n"
    print(visual_board)

    # -------Se comprueba jugador-------

    if is_player1:
        player_symbol = player1_symbol
    else:
        player_symbol = player2_symbol

    # -------Introducción de posiciones-------

    while True:
        row_position = int(input("Introduzca fila y columna:\nFila:"))
        column_position = int(input("Columna:"))

        # -------Comprueba que la posición es correcta-------

        if not (0 <= row_position < size and 0 <= column_position < size):
            print("Error. Estás fuera del tablero")
        elif (
            board[row_position][column_position] != f"{row_position},{column_position}"
        ):
            print("Error. Ya existe una ficha en esta posición.")
        else:
            decisions[is_player1] = board[row_position][column_position]
            board[row_position][column_position] = player_symbol
            is_player1 = not is_player1
            break

# -------Condiciones de victoria-------
