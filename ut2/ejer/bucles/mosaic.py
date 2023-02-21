n = 5

for i in range(n):
    line = ""
    for j in range(n):
        if j == i:
            line += "X  "
        else:
            if j > i:
                line += "U  "
            else:
                line += "D  "
    print(line + "\n")
