from copy import copy, deepcopy

flippedPositions = {}

def flipTile(q, r, map):
    initTile(q, r, map)
    if map[q][r] == 1:
        map[q][r] = 0
    else:
        map[q][r] = 1

def setTile(q, r, map, value):
    initTile(q, r, map)
    map[q][r] = value

def initTile(q, r, map):
    if q not in map:
        map[q] = {}
    if r not in map[q]:
        map[q][r] = 1 # init to white side up

# f = open("exampleInput.txt", "r")
f = open("input.txt", "r")
for line in f.readlines():
    q = 0
    r = 0
    strippedLine = line.strip()
    print(strippedLine)
    remainingString = strippedLine
    while remainingString is not None and len(remainingString) > 0:
        # print(remainingString)
        twoChars = remainingString[0:2]
        oneChar = remainingString[0:1]
        if twoChars == 'ne':
            q = q + 1
            r = r - 1
            remainingString = remainingString[2:]
        elif twoChars == 'nw':
            r = r - 1
            remainingString = remainingString[2:]
        elif twoChars == 'se':
            r = r + 1
            remainingString = remainingString[2:]
        elif twoChars == 'sw':
            q = q - 1
            r = r + 1
            remainingString = remainingString[2:]
        elif oneChar == 'e':
            q = q + 1
            remainingString = remainingString[1:]
        elif oneChar == 'w':
            q = q - 1
            remainingString = remainingString[1:]
        else:
            exit()
    flipTile(q, r, flippedPositions)

print(flippedPositions)
flippedCount = 0
for q, col in flippedPositions.items():
    for r, tile in col.items():
        if tile == 0:
            flippedCount = flippedCount + 1

def isTileBlack(q, r, map):
    if q not in map:
        return False
    if r not in map[q]:
        return False
    return map[q][r] == 0

def countBlackNeighbors(q, r, map):
    neighborCount = 0
    dirs = [[1, -1], [0, -1], [0, 1], [-1, 1], [1, 0], [-1, 0]]
    for dir in dirs:
        if isTileBlack(q + dir[0], r + dir[1], map):
            neighborCount = neighborCount + 1
    return neighborCount

def fillNeighborsOfBlacks(map):
    # return map
    newMap = deepcopy(map)
    for q, col in map.items():
        for r, tile in col.items():
            if isTileBlack(q, r, map):
                dirs = [[1, -1], [0, -1], [0, 1], [-1, 1], [1, 0], [-1, 0]]
                for dir in dirs:
                    initTile(q + dir[0], r + dir[1], newMap)
    return newMap


print(flippedCount)
flippedPositions = fillNeighborsOfBlacks(flippedPositions)
lastConfiguration = flippedPositions
for i in range(1, 101):
    # print(lastConfiguration)
    # print(i)
    nextConfiguration = deepcopy(lastConfiguration)
    for q, col in lastConfiguration.items():
        for r, tile in col.items():
            blackNeighborsCount = countBlackNeighbors(q, r, lastConfiguration)
            # print(blackNeighborsCount)
            if isTileBlack(q, r, lastConfiguration):
                if blackNeighborsCount == 0 or blackNeighborsCount > 2:
                    # print("flip black to white")
                    # flipTile(q, r, nextConfiguration)
                    setTile(q, r, nextConfiguration, 1)
            else:
                if blackNeighborsCount == 2:
                    # print("flip white to black")
                    setTile(q, r, nextConfiguration, 0)
                    # flipTile(q, r, nextConfiguration)
    lastConfiguration = fillNeighborsOfBlacks(nextConfiguration)
    flippedCount = 0
    for q, col in lastConfiguration.items():
        for r, tile in col.items():
            if tile == 0:
                flippedCount = flippedCount + 1
    print(flippedCount)
