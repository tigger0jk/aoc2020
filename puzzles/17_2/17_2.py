from copy import copy, deepcopy

dim = {}
dim[0] = {} # starting plane
dim[0][0] = {} # starting plane

xMin = 0
xMax = 0
yMin = 0
yMax = 0
zMin = 0
zMax = 0
wMin = 0
wMax = 0

f = open("input.txt", "r")
# f = open("exampleInput.txt", "r")
z = 0

def setDim(dim, x, y, z, w, val):
    # print(str(x) + ", " + str(y) + ", " + str(z) + " = " + val)
    global xMin, xMax, yMin, yMax, zMin, zMax, wMin, wMax
    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y
    if z < zMin:
        zMin = z
    if z > zMax:
        zMax = z
    if w < wMin:
        wMin = w
    if w > wMax:
        wMax = w
    if x not in dim:
        dim[x] = {}
    if y not in dim[x]:
        dim[x][y] = {}
    if z not in dim[x][y]:
        dim[x][y][z] = {}
    dim[x][y][z][w] = val

for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    dim[0][0][z] = {}
    vals = list(strippedLine)
    for w in range(len(vals)):
        setDim(dim, 0, 0, z, w, vals[w])
    z = z + 1

def isActive(dim, x, y, z, w):
    return x in dim and y in dim[x] and z in dim[x][y] and w in dim[x][y][z] and dim[x][y][z][w] == "#"


def countActiveNeighbors(dim, x, y, z, w):
    neighborCount = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for m in range(-1, 2):
                    if 0 == i == j == k == m:
                        continue
                    if isActive(dim, x + i, y + j, z + k, w + m):
                        neighborCount = neighborCount + 1
    return neighborCount

def countActiveCubes(dim):
    activeCubesCount = 0
    for x in range(xMin, xMax + 1):
        for y in range(yMin, yMax + 1):
            for z in range(zMin, zMax + 1):
                for w in range(wMin, wMax + 1):
                    if isActive(dim, x, y, z, w):
                        # print(str(x) + ", " + str(y) + ", " + str(z))
                        activeCubesCount = activeCubesCount + 1
    return activeCubesCount

# didn't update to 4D
# def printDims(dim):
    # for x in range(xMin, xMax + 1):
        # print(x)
        # for y in range(yMin, yMax + 1):
            # row = ''
            # for z in range(zMin, zMax + 1):
                # if isActive(dim, x, y, z):
                    # row = row + '#'
                # else:
                    # row = row + '.'
            # print(row)

print(dim)
lastConfiguration = dim
print("Active cubes count: " + str(countActiveCubes(lastConfiguration)))
for cycle in range(1, 7):
    nextConfiguration = deepcopy(lastConfiguration)
    for x in range(xMin - 1, xMax + 2):
        for y in range(yMin - 1, yMax + 2):
            for z in range(zMin - 1, zMax + 2):
                for w in range(wMin - 1, wMax + 2):
                    activeNeighborsCount = countActiveNeighbors(lastConfiguration, x, y, z, w)
                    if isActive(lastConfiguration, x, y, z, w):
                        if activeNeighborsCount == 2 or activeNeighborsCount == 3:
                            setDim(nextConfiguration, x, y, z, w, '#') # stay active, noop
                        else:
                            setDim(nextConfiguration, x, y, z, w, '.') # deactivate
                    else:
                        if activeNeighborsCount == 3:
                            setDim(nextConfiguration, x, y, z, w, '#') # activate

    lastConfiguration = nextConfiguration
    print("Active cubes count: " + str(countActiveCubes(lastConfiguration)))

# printDims(lastConfiguration)
print("Active cubes count: " + str(countActiveCubes(lastConfiguration)))
