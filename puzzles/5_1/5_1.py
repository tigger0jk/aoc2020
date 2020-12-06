maxId = 0
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
    print("Id: " + str(id))
    # print(passRow)
    # print(passCol)

# F = 0
# B = 1

# R = 1
# L = 0

print("Max id: " + str(maxId))
