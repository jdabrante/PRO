board = []


size = int(input("¿Que n en raya desea jugar?:"))

# -------Se crea el tablero-------

for row in range(size):
    board.append([])
    for column in range(size):
        board[row].append(f"{row},{column} ")

# -------Se inicializa las variables de juego-------

is_player2 = False
player1_symbol = " ❌ "
player2_symbol = " ⭕ "
decisions = ["", ""]
winner = 0

# -------Se imprime el tablero inicial para mejor visión del usuario-------
visual_board = ""
for row in board:
    visual_board += " | ".join(row) + "\n\n"
print(visual_board)


# -------Juego-------
positions_amount = size * size
for turn in range(positions_amount):
    visual_board = ""

    # -------Se comprueba jugador-------

    if is_player2:
        player_symbol = player2_symbol
    else:
        player_symbol = player1_symbol

    # -------Introducción de posiciones-------

    while True:
        row_position = int(
            input(f"Introduzca fila y columna jugador{is_player2+1}:\nFila:")
        )
        column_position = int(input("Columna:"))

        # -------Comprueba que la posición es correcta-------

        if not (0 <= row_position < size and 0 <= column_position < size):
            print("Error. Estás fuera del tablero")
        elif (
            board[row_position][column_position] != f"{row_position},{column_position} "
        ):
            print("Error. Ya existe una ficha en esta posición.")
        else:
            decisions[is_player2] += board[row_position][column_position] + " "
            board[row_position][column_position] = player_symbol
            break

    # -------Condiciones de victoria-------
    diagonal_positions1 = False
    diagonal_positions2 = False
    inverse_diagonal_row = size - 1
    inverse_diagonal_column = 0
    inverse_positions1 = 0
    inverse_positions2 = 0
    if turn >= size - 1:
        for i in range(size):
            is_win_condition = decisions[0].count(f"{i},") == size
            is_win_condition1 = decisions[0].count(f",{i}") == size or is_win_condition
            is_win_condition = decisions[1].count(f"{i},") == size
            is_win_condition2 = decisions[1].count(f",{i}") == size or is_win_condition

            # La diagonal principal cumple con lo siguiente: (1,1)(2,2)(3,3)...
            diagonal_positions1 += decisions[0].count(f"{i},{i}")
            diagonal_positions2 += decisions[1].count(f"{i},{i}")
            is_diagonal = diagonal_positions1 == size or diagonal_positions2 == size

            inverse_positions1 += decisions[0].count(
                f"{inverse_diagonal_row},{inverse_diagonal_column}"
            )
            inverse_positions2 += decisions[1].count(
                f"{inverse_diagonal_row},{inverse_diagonal_column}"
            )
            is_diagonal_inverse = (
                inverse_positions1 == size or inverse_positions2 == size
            )
            # La diagonal inversa cumple de arriba a abajo lo siguiente: (3,0)(2,1)(1,2)(0,3) (se va restando la fila y sumando la columna)
            inverse_diagonal_row -= 1
            inverse_diagonal_column += 1

            if any(
                [is_win_condition1, is_win_condition2, is_diagonal, is_diagonal_inverse]
            ):
                winner = is_player2 + 1
                break

    # -------Se imprime el tablero -------
    visual_board = ""
    for row in board:
        visual_board += " | ".join(row) + "\n\n"
    print(visual_board)

    # Se comprueba si hay ganador

    if winner > 0:
        print(f"El jugador{winner} ha ganado")
        break

    # -------Se cambia de turno-------

    is_player2 = not is_player2
else:
    print("Empate")
