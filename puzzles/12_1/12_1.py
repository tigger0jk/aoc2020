import re

def moveDir(pos, dir, value):
    if (dir == 0):
        pos[0] = pos[0] + value
    elif (dir == 180):
        pos[0] = pos[0] - value
    elif (dir == 90):
        pos[1] = pos[1] + value
    elif (dir == 270):
        pos[1] = pos[1] - value


# [NS / EW]
pos = [0, 0]
dir = 90
f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    res = re.search("^(\w)(\d*)$", strippedLine)
    letter = res.group(1)
    value = int(res.group(2))
    print("Letter: " + letter)
    print("Letter: " + str(value))
    if (letter == 'F'):
        moveDir(pos, dir, value)
    if (letter == 'N'):
        moveDir(pos, 0, value)
    if (letter == 'E'):
        moveDir(pos, 90, value)
    if (letter == 'S'):
        moveDir(pos, 180, value)
    if (letter == 'W'):
        moveDir(pos, 270, value)
    if (letter == 'L'):
        dir = (dir - value) % 360
    if (letter == 'R'):
        dir = (dir + value) % 360
    print("dir: " + str(dir))
    print(pos)

print("final loc: ")
print(pos)
print("manhattan: " + str(abs(pos[0]) + abs(pos[1])))
