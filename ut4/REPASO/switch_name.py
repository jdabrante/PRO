# ************************
# INTERCAMBIANDO TU NOMBRE
# ************************

full_name = lambda fn,sn: f'{sn}, {fn}'

def run(first_name: str, surname: str) -> str:
    return full_name(first_name,surname)


if __name__ == '__main__':
    run('Sergio', 'Delgado Quintero')