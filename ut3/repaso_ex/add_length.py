# *********************
# PALABRAS CON LONGITUD
# *********************


# def run(text: str) -> list:
#     text = text.split()
#     words_length = []
#     for word in text:
#         word_length = len(word)
#         word += f" {word_length}"
#         words_length.append(word)

#     return words_length


def run(text: str) -> list:
    text = text.split()
    words_length = []
    for word in text:
        word += f" {len(word)}"
        words_length.append(word)

    return words_length


if __name__ == "__main__":
    run("todo se transforma")
