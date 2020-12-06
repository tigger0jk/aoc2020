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
inputHeight = len(treeMap)
print(inputHeight)
print(inputWidth)

def getTreeCount(tobogganXOffset, tobogganYOffset = 1):
    treeCount = 0
    tobogganIndex = 0
    for rowIndex in range(inputHeight):
        if rowIndex % tobogganYOffset != 0:
            continue
        treeRow = treeMap[rowIndex]
        if (treeRow[tobogganIndex]):
            treeCount = treeCount + 1
        tobogganIndex = (tobogganIndex + tobogganXOffset) % inputWidth

    print("trees hit: " + str(treeCount))
    return treeCount

product = getTreeCount(1, 1)
product = product * getTreeCount(3, 1)
product = product * getTreeCount(5, 1)
product = product * getTreeCount(7, 1)
product = product * getTreeCount(1, 2)
print(product)

