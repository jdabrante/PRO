# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    initials = (fullname.split(",")[0]).strip().split(" ")
    initials.insert(0,fullname.split(",")[1].strip())
    return f'{".".join([(word[0]).upper() for word in initials])}.'


if __name__ == '__main__':
    run('Delgado Quintero, sergio')