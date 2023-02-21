# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    text = []
    for code in hex_codes:
        value_code = int(code, 16)
        text.append(chr(value_code))
    text = "".join(text)

    return text


if __name__ == "__main__":
    run(["1f49a", "2728", "1f389", "1f3c6"])
