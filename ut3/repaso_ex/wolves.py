# **************
# EL LOBO ACECHA
# **************


def run(farm: list) -> str:
    farm.reverse()

    if farm[0] != "lobo":
        for i, animal in enumerate(farm):
            if animal == "lobo":
                sheep = i
        msg = f"Cuidado oveja {sheep}, el lobo te va a comer"
    else:
        msg = "No te quiero ver más por aquí, lobo"

    return msg


if __name__ == "__main__":
    run(["oveja", "oveja", "lobo", "oveja"])
