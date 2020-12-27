flippedPositions = {}

def flipTile(q, r):
    if q not in flippedPositions:
        flippedPositions[q] = {}
    if r not in flippedPositions[q]:
        flippedPositions[q][r] = 1 # init to white side up
    if flippedPositions[q][r] == 1:
        flippedPositions[q][r] = 0
    else:
        flippedPositions[q][r] = 1

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
    flipTile(q, r)

print(flippedPositions)
flippedCount = 0
for q, col in flippedPositions.items():
    for r, tile in col.items():
        if tile == 0:
            flippedCount = flippedCount + 1

print(flippedCount)
