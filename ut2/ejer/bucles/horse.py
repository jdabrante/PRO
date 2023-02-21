x = 7
y = 8
position_x = 0

position_y = 0


while position_x < x and position_y < y:
    print(f"({position_x},{position_y})", end=" ")
    position_x += 1
    position_y += 2
    print(f"({position_x},{position_y})", end=" ")
    position_x += 2
    position_y += 1

# flow = True
# while position_x < x and position_y < y:
#   print(f"{x},{y}")
#   position_x += 2 - flow
#   position_y += 1 + flow
#   flow = not flow
