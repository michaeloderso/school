input_data = [
[[0, 9], [5, 9]],
[[8, 0], [0, 8]],
[[9, 4], [3, 4]],
[[2, 2], [2, 1]],
[[7, 0], [7, 4]],
[[6, 4], [2, 0]],
[[0, 9], [2, 9]],
[[3, 4], [1, 4]],
[[0, 0], [8, 8]],
[[5, 5], [8, 2]]
]


control_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Smaller number first
def sortnumber(xy1, xy2):
    if xy1 <= xy2:
        return xy1, xy2
    else:
        return xy2, xy1


for count, compare in enumerate(input_data):
    coordinate1, coordinate2 = input_data[count]
    x1, x2 = sortnumber(coordinate1[0], coordinate2[0])
    y1, y2 = sortnumber(coordinate1[1], coordinate2[1])

    if y1 == y2: # Horizontale Linie
        x_counter = x1
        for increase in range(x1, x2 + 1):
            new_line = control_grid[y1]
            new_line[x_counter] += 1
            control_grid[y1] = new_line
            x_counter += 1

    elif x1 == x2: # Vertikale Linie
        y_counter = y1
        for increase in range(y1, y2 + 1):
            new_line = control_grid[y_counter]
            new_line[x1] += 1
            control_grid[y_counter] = new_line
            y_counter += 1


overlap_counter = 0
for count, eachline in enumerate(control_grid):
    line = control_grid[count]
    for count2, eachnumber in enumerate(line):
        if line[count2] >= 2:
            overlap_counter += 1

print(f"There are {overlap_counter} overlaps")



