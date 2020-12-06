maxId = 0
minId = 0b1111111111 + 1
takenIds = {}
f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    boardingPass = strippedLine
    passRow = boardingPass[0:7]
    passRow = passRow.replace('F', '0')
    passRow = passRow.replace('B', '1')
    row = int(passRow, 2)
    print("Row: " + str(row))
    passCol = boardingPass[-3:]
    passCol = passCol.replace('R', '1')
    passCol = passCol.replace('L', '0')
    col = int(passCol, 2)
    print("Col: " + str(col))
    id = row * 8 + col
    if (id > maxId):
        maxId = id
    if (id < minId):
        minId = id
    takenIds[id] = True
    print("Id: " + str(id))
    # print(passRow)
    # print(passCol)

# F = 0
# B = 1

# R = 1
# L = 0

for id in range(0b1111111111):
    if id not in takenIds.keys():
        if id < maxId and id > minId:
            print("Possible id: " + str(id))

print("Max id: " + str(maxId))
