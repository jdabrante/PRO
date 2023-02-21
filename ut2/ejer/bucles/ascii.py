INITIAL_CODE = 33
FINAL_CODE = 127
num_chars = 0
LINE_SIZE = 5
row = ""
for number in range(INITIAL_CODE, FINAL_CODE + 1):
    sing = chr(number)
    row += f"{number:03d} {sing} "
    num_chars += 1
    if num_chars % LINE_SIZE == 0:
        print(row)
        row = ""  # Se limpia la variable row una vez se da el if
