# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    # TU C�DIGO AQU�
    text = ''
    for value in hex_codes:
        text += chr(int(value,16))
    return text


if __name__ == '__main__':
    run(['1f49a', '2728', '1f389', '1f3c6'])