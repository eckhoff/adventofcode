xmas_matrix = []
with open('test.txt', 'r') as file:
    for line in file:
        stripped_line = line.strip()
        row = list(stripped_line)
        xmas_matrix.append(row)
'''
for i in xmas_matrix:
    for j in range(len(i)):
        if i[j] == 'X':
            try:
                if i[j+1] == 'M' and i[j+2] == 'A' and i[j+3] == 'S':
                    print(i[j] + i[j+1] + i[j+2] + i[j+3])
            except IndexError:
                pass
            try:
                if i[j-1] == 'M' and i[j-2] == 'A' and i[j-3] == 'S':
                    print(i[j] + i[j-1] + i[j-2] + i[j-3])
            except IndexError:
                pass
'''
result = 0
for i in range(len(xmas_matrix)):
    for j in range(len(xmas_matrix[i])):
        if xmas_matrix[i][j] == 'X':
            try:
                if xmas_matrix[i][j+1] == 'M' and xmas_matrix[i][j+2] == 'A' and xmas_matrix[i][j+3] == 'S':
                    result += 1
            except IndexError:
                pass
            try:
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
                if xmas_matrix[i-1][j-1] == 'M' and xmas_matrix[i-2][j-2] == 'A' and xmas_matrix[i-3][j-3] == 'S':
                    result += 1
            except IndexError:
                pass
            try:
                if xmas_matrix[i+1][j-1] == 'M' and xmas_matrix[i+2][j-2] == 'A' and xmas_matrix[i+3][j-3] == 'S':
                    result += 1
            except IndexError:
                pass
            try:
                if xmas_matrix[i-1][j+1] == 'M' and xmas_matrix[i-2][j+2] == 'A' and xmas_matrix[i-3][j+3] == 'S':
                    result += 1
            except IndexError:
                pass

print(result)
            