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

def diagonal_check(x1, x2, y1, y2):
    bool1 = False
    bool2 = False
    if x1 < x2: # Left to Right
        bool1 = True
    if y1 < y2: # Top to Bottom
        bool2 = True
    return bool1, bool2

for count, compare in enumerate(input_data):
    coordinate1, coordinate2 = input_data[count]
    x1, x2 = sortnumber(coordinate1[0], coordinate2[0])
    y1, y2 = sortnumber(coordinate1[1], coordinate2[1])

    # Horizontale Linie
    if y1 == y2:
        x_counter = x1
        for increase in range(x1, x2 + 1):
            new_line = control_grid[y1]
            new_line[x_counter] += 1
            control_grid[y1] = new_line
            x_counter += 1
    # Vertikale Linie
    elif x1 == x2:
        y_counter = y1
        for increase in range(y1, y2 + 1):
            new_line = control_grid[y_counter]
            new_line[x1] += 1
            control_grid[y_counter] = new_line
            y_counter += 1
    # Diagonale Linie
    else:
        lefttoright, toptobottom = diagonal_check(coordinate1[0], coordinate2[0], coordinate1[1], coordinate2[1])
        for increase in range(y1, y2 + 1):
            new_line = control_grid[y1]
            if (toptobottom == True and lefttoright == True) or (toptobottom == False and lefttoright == False):
                new_line[x1] += 1
                control_grid[y1] = new_line
                x1 += 1
                y1 += 1
            elif (toptobottom == True and lefttoright == False) or (toptobottom == False and lefttoright == True):
                new_line[x2] += 1
                control_grid[y1] = new_line
                x2 -= 1
                y1 += 1


overlap_counter = 0
for count, eachline in enumerate(control_grid):
    line = control_grid[count]
    for count2, eachnumber in enumerate(line):
        if line[count2] >= 2:
            overlap_counter += 1


# for counting, eachline in enumerate(control_grid):
#        print(control_grid[counting])
print(f"There are {overlap_counter} overlaps")




