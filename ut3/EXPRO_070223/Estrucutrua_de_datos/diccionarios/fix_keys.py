# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    # TU C�DIGO AQU�
    fitems = {}
    for key,value in items.items():
        new_key = key.replace(" ","")
        fitems[new_key] = value
    return fitems


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})