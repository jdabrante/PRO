# *************************
# PALABRAS EN ORDEN INVERSO
# *************************


def run(text: str) -> str:
    text = text.lower()
    text = text.split()
    text.reverse()

    reversing = " ".join(text)

    return reversing


if __name__ == "__main__":
    run("Hello World")
