# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    initial = []
    fullname = fullname.upper()
    fullname_list = fullname.split(",")
    name = fullname_list[1].strip()
    full_surname = fullname_list[0].split()

    initial_name = name[0]
    initial_surname1 = full_surname[0][0]

    if len(full_surname) > 1:
        initial_surname2 = full_surname[1][0]
        initials = f"{initial_name}.{initial_surname1}.{initial_surname2}."
    else:
        initials = f"{initial_name}.{initial_surname1}."

    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
