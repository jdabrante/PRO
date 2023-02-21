# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    games_player1 = games_player2 = "tu código aquí"
    a_points = 0
    b_points = 0
    games_player1 = 0
    games_player2 = 0
    a_set = 0
    b_set = 0
    tie_break = False
    target_score = 6 + tie_break

    for point in points:
        if point == "A":
            a_points += 1
        else:
            b_points += 1

        if a_points >= 4 or b_points >= 4:
            # En el caso de que A sea el ganador del juego
            if a_points - b_points >= 2:
                games_player1 += 1
                a_points = b_points = 0
                if (
                    games_player1 >= 6
                    and (games_player1 - games_player2 >= 2)
                    and tie_break == False
                ):
                    a_set += 1
                    games_player1 = games_player2 = 0
                    if a_set == 2:
                        winner = "A"
                        break
                # En el caso de que se produzca un tie break
                elif tie_break == True:
                    if games_player1 >= 7 and (games_player1 - games_player2 >= 2):
                        a_set += 1
                        games_player1 = games_player2 = 0
                        tie_break = False
                        if a_set == 2:
                            winner = "A"
                            break
                # Condición cuando se cumple un empate y por lo tanto dará lugar a un tie break
                elif games_player1 == 6 and games_player2 == 6:
                    tie_break = True
                    games_player1 = games_player2 = 0
            # En el caso de que B sea el ganador del juego
            if b_points - a_points >= 2:
                games_player2 += 1
                a_points = b_points = 0
                if (
                    games_player2 >= 6
                    and (games_player2 - games_player1 >= 2)
                    and tie_break == False
                ):
                    b_set += 1
                    games_player1 = games_player2 = 0
                    if b_set == 2:
                        winner = "B"
                        break
                # En el caso de que se produzca un tie break
                elif tie_break == True:
                    if games_player2 >= 7 and (games_player2 - games_player1 >= 2):
                        games_player1 = games_player2 = 0
                        b_set += 1
                        tie_break = False
                        if b_set == 2:
                            winner = "B"
                            break
                # Condición cuando se cumple un empate y por lo tanto dará lugar a un tie break
                elif games_player1 == 6 and games_player2 == 6:
                    tie_break = True
                    games_player1 = games_player2 = 0

    return games_player1, games_player2


if __name__ == "__main__":
    run("AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB")
