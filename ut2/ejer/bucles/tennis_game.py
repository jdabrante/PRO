# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    winner = "tu código aquí"
    a_points = 0
    b_points = 0
    a_game = 0
    b_game = 0
    a_set = 0
    b_set = 0
    tie_break = False

    for point in points:
        if point == "A":
            a_points += 1
        else:
            b_points += 1

        if a_points >= 4 or b_points >= 4:
            # En el caso de que A sea el ganador del juego
            if a_points - b_points >= 2:
                a_game += 1
                a_points = b_points = 0
                if a_game >= 6 and (a_game - b_game >= 2) and tie_break == False:
                    a_set += 1
                    a_game = b_game = 0
                    if a_set == 2:
                        winner = "A"
                        break
                # En el caso de que se produzca un tie break
                elif tie_break == True:
                    if a_game >= 7 and (a_game - b_game >= 2):
                        a_set += 1
                        a_game = b_game = 0
                        tie_break = False
                        if a_set == 2:
                            winner = "A"
                            break
                # Condición cuando se cumple un empate y por lo tanto dará lugar a un tie break
                elif a_game == 6 and b_game == 6:
                    tie_break = True
                    a_game = b_game = 0
            # En el caso de que B sea el ganador del juego
            if b_points - a_points >= 2:
                b_game += 1
                a_points = b_points = 0
                if b_game >= 6 and (b_game - a_game >= 2) and tie_break == False:
                    b_set += 1
                    a_game = b_game = 0
                    if b_set == 2:
                        winner = "B"
                        break
                # En el caso de que se produzca un tie break
                elif tie_break == True:
                    if b_game >= 7 and (b_game - a_game >= 2):
                        a_game = b_game = 0
                        b_set += 1
                        tie_break = False
                        if b_set == 2:
                            winner = "B"
                            break
                # Condición cuando se cumple un empate y por lo tanto dará lugar a un tie break
                elif a_game == 6 and b_game == 6:
                    tie_break = True
                    a_game = b_game = 0

    return winner


if __name__ == "__main__":
    run(
        "AAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBB"
    )
