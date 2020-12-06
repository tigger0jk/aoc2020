treeMap = []

f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    treeRow = []
    for char in strippedLine:
        if char == '.':
            treeRow.append(False)
        elif char == '#':
            treeRow.append(True)
        else:
            print("ERROR: INVALID CHAR FOUND ===================")
    treeMap.append(treeRow)

inputWidth = len(treeMap[0])
print(len(treeMap))
print(inputWidth)

treeCount = 0
tobogganXOffset = 3
tobogganIndex = 0
for treeRow in treeMap:
    if (treeRow[tobogganIndex]):
        treeCount = treeCount + 1
    tobogganIndex = (tobogganIndex + tobogganXOffset) % inputWidth

print("trees hit: " + str(treeCount))
