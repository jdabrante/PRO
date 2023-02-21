target_x = 7
target_y = 8
x = 0
y = 0
print(f'({x},{y}) ', end="")
change = True
while  x != target_x and y != target_y:
        if target_x > target_y:
            x += 1 + change
            y += 2 - change
        else: 
             x += 2 - change
             y += 1 + change
        if change:
            change = False
        else: 
            change = True
        print(f'({x},{y}) ', end="")


