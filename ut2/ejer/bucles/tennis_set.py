# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    games_player1 = games_player2 = "tu código aquí"

    points_player1 = 0
    points_player2 = 0
    games_player1 = 0
    games_player2 = 0
    tie_break = False
    target_score = 4 + tie_break
    target_game = 6

    for point in points:
        if point == "A":
            points_player1 += 1
        else:
            points_player2 += 1

        # Gana el juego A

        if points_player1 >= target_score or points_player2 >= target_score:
            if points_player1 - points_player2 >= 2:
                games_player1 += 1
                points_player1 = points_player2 = 0
                if (games_player1 >= target_game) and (
                    games_player1 - games_player2 >= 2
                ):
                    break
                elif games_player1 == games_player2 == 6:
                    tie_break = True

            # Gana el juego B

            if points_player2 - points_player1 >= 2:
                games_player2 += 1
                points_player1 = points_player2 = 0
                if (games_player2 >= target_game) and (
                    games_player2 - games_player1 >= 2
                ):
                    break
                elif games_player1 == games_player2 == 6:
                    tie_break = True

    return games_player1, games_player2


if __name__ == "__main__":
    run("AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB")
