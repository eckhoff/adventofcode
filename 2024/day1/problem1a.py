totalDistance = 0
listLeft = []
listRight = []

with open('problem1a-input.txt', 'r') as file:
    for line in file:
        value1, value2 = line.split()
        value1 = int(value1)
        value2 = int(value2)
        listLeft.append(value1)
        listRight.append(value2)

listLeft.sort()
listRight.sort()

result = [abs(a - b) for a, b in zip(listLeft, listRight)]

print(sum(result))
