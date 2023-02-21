"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    uppername = fullname.upper()
    name_list = uppername.split(", ")
    first_name = name_list[1][0]
    full_surname = name_list[0]
    surname_list = full_surname.split()

    if len(surname_list) > 1:

        first_surname = surname_list[0][0]
        second_surname = surname_list[1][0]
        initials = f"{first_name}.{first_surname}.{second_surname}."
    else:
        first_surname = surname_list[0][0]
        initials = f"{first_name}.{first_surname}."
    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
