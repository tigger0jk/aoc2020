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

def rotateVec(vec, degrees):
    if (degrees == 0):
        #noop
        vec = vec
    elif (degrees == 180):
        vec = [-vec[0], -vec[1]]
    elif (degrees == 90):
        vec = [-vec[1], vec[0]]
    elif (degrees == 270):
        vec = [vec[1], -vec[0]]
    return vec

# [NS / EW]
pos = [0, 0]
way = [1, 10]
#  dir = 90
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
        pos[0] = pos[0] + way[0] * value
        pos[1] = pos[1] + way[1] * value
    if (letter == 'N'):
        moveDir(way, 0, value)
    if (letter == 'E'):
        moveDir(way, 90, value)
    if (letter == 'S'):
        moveDir(way, 180, value)
    if (letter == 'W'):
        moveDir(way, 270, value)
    if (letter == 'L'):
        print("rotate vec left by " + str(value) + " aka " + str((360 - value) % 360))
        way = rotateVec(way, (360 - value) % 360) # mod probably not required
    if (letter == 'R'):
        print("rotate vec right by " + str(value) + " aka " + str(value % 360))
        way = rotateVec(way, value % 360)
    #  print("dir: " + str(dir))
    print(way)
    print(pos)

print("final loc: ")
print(pos)
print("manhattan: " + str(abs(pos[0]) + abs(pos[1])))
