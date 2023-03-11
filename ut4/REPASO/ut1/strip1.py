# *************************
# QUITANDO PRIMERO Y �LTIMO
# *************************


def run(text: str) -> str:
    return text[1:len(text)-1]
if __name__ == '__main__':
    run('What can I do')