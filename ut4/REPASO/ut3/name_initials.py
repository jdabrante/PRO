# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    initials = (fullname.split(",")[0]).strip().split(" ")
    initials.insert(0,fullname.strip().split(",")[1])
    return ".".join([(word[0]).upper() for word in initials])


if __name__ == '__main__':
    run('Delgado Quintero, sergio')