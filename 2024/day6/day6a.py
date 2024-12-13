grid = []

with open('input.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        row = list(stripped_line)
        grid.append(row)

def starting_point(matrix):
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            if matrix[row][element] == '^':
                return row, element

def move(matrix):
    location = starting_point(matrix)
    location_lst = []

    while True:
        while matrix[location[0]][location[1]] != '#':
            location_lst.append(location)
            location = move_up(matrix, location[0], location[1])
            if location == False:
                break
        if location == False:
            break
        location = move_down(matrix, location[0], location[1])

        while matrix[location[0]][location[1]] != '#':
            location_lst.append(location)
            location = move_right(matrix, location[0], location[1])
            if location == False:
                break
        if location == False:
            break
        location = move_left(matrix, location[0], location[1])

        while matrix[location[0]][location[1]] != '#':
            location_lst.append(location)
            location = move_down(matrix, location[0], location[1])
            if location == False:
                break
        if location == False:
            break 
        location = move_up(matrix, location[0], location[1])

        while matrix[location[0]][location[1]] != '#':
            location_lst.append(location)
            location = move_left(matrix, location[0], location[1])
            if location == False:
                break
        if location == False:
            break
        location = move_right(matrix, location[0], location[1])

    return location_lst        


def move_up(matrix, x, y):
    try:
        if x-1 >= 0:
            new_location = (x-1, y)
            matrix[new_location[0]][new_location[1]]
            return new_location
        else:
            return False
    except IndexError:
        return False
    
def move_right(matrix, x,y):
    try:
        new_location = (x, y+1)
        matrix[new_location[0]][new_location[1]]
        return new_location
    except IndexError:
        return False
    
def move_down(matrix, x,y):
    try:
        new_location = (x+1, y)
        matrix[new_location[0]][new_location[1]]
        return new_location
    except IndexError:
        return False

def move_left(matrix, x,y):
    try:
        if y >= 0:
            new_location = (x, y-1)
            matrix[new_location[0]][new_location[1]]
            return new_location
        else:
            return False
    except IndexError:
        return False

def unique_points(matrix):
    unique_nums = set(matrix)
    return len(unique_nums)


result = unique_points(move(grid))
print(result)
