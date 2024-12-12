xmas_matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        row = list(stripped_line)
        xmas_matrix.append(row)


result = 0

for i in range(len(xmas_matrix)):
    for j in range(len(xmas_matrix[i])):
        if xmas_matrix[i][j] == 'A':
            try:
                if i-1 >=0 and j-1 >=0:
                    if xmas_matrix[i-1][j+1] == 'M' and xmas_matrix[i+1][j-1] == 'S':
                        if xmas_matrix[i-1][j-1] == 'M' and xmas_matrix[i+1][j+1] == 'S':
                            result += 1
                        elif xmas_matrix[i-1][j-1] == 'S' and xmas_matrix[i+1][j+1] == 'M':
                            result += 1
                    elif xmas_matrix[i-1][j+1] == 'S' and xmas_matrix[i+1][j-1] == 'M':
                        if xmas_matrix[i-1][j-1] == 'M' and xmas_matrix[i+1][j+1] == 'S':
                            result += 1
                        elif xmas_matrix[i-1][j-1] == 'S' and xmas_matrix[i+1][j+1] == 'M':
                            result += 1
            except IndexError:
                pass
            '''
            try:
                if i-1 >=0 and i-2 >=0 and i-3 >=0 and j-1 >=0 and j-2 >=0 and j-3 >=0:
                    if xmas_matrix[i-1][j-1] == 'M' and xmas_matrix[i+1][j+1] == 'S':
                        result += 1
                    elif xmas_matrix[i-1][j-1] == 'S' and xmas_matrix[i+1][j+1] == 'M':
                        result += 1
            except IndexError:
                pass
'''


'''
            try:
                if j-1 >=0 and j-2 >=0 and j-3 >=0:
                    if xmas_matrix[i][j-1] == 'M' and xmas_matrix[i][j-2] == 'A' and xmas_matrix[i][j-3] == 'S':
                        result += 1
            except IndexError:
                pass
            try:
                if xmas_matrix[i+1][j] == 'M' and xmas_matrix[i+2][j] == 'A' and xmas_matrix[i+3][j] == 'S':
                    result += 1
            except IndexError:
                pass
            try:
                if i-1 >=0 and i-2 >=0 and i-3 >=0:
                    if xmas_matrix[i-1][j] == 'M' and xmas_matrix[i-2][j] == 'A' and xmas_matrix[i-3][j] == 'S':
                        result += 1
            except IndexError:
                pass
            try:
                if xmas_matrix[i+1][j+1] == 'M' and xmas_matrix[i+2][j+2] == 'A' and xmas_matrix[i+3][j+3] == 'S':
                    result += 1
            except IndexError:
                pass
            try:
                if i-1 >=0 and j-1 >=0 and i-2 >=0 and j-2 >=0 and i-3 >=0 and j-3 >=0:
                    if xmas_matrix[i-1][j-1] == 'M' and xmas_matrix[i-2][j-2] == 'A' and xmas_matrix[i-3][j-3] == 'S':
                        result += 1
            except IndexError:
                pass
            try:
                if j-1 >=0 and j-2 >=0 and j-3 >=0:
                    if xmas_matrix[i+1][j-1] == 'M' and xmas_matrix[i+2][j-2] == 'A' and xmas_matrix[i+3][j-3] == 'S':
                        result += 1
            except IndexError:
                pass
            try:
                if i-1 >=0 and i-2 >=0 and i-3 >=0:
                    if xmas_matrix[i-1][j+1] == 'M' and xmas_matrix[i-2][j+2] == 'A' and xmas_matrix[i-3][j+3] == 'S':
                        result += 1
            except IndexError:
                pass
'''
print(result) 