from copy import copy, deepcopy

dim = {}
dim[0] = {} # starting plane

xMin = 0
xMax = 0
yMin = 0
yMax = 0
zMin = 0
zMax = 0

f = open("input.txt", "r")
# f = open("exampleInput.txt", "r")
y = 0

def setDim(dim, x, y, z, val):
    # print(str(x) + ", " + str(y) + ", " + str(z) + " = " + val)
    global xMin, xMax, yMin, yMax, zMin, zMax
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
    if x not in dim:
        dim[x] = {}
    if y not in dim[x]:
        dim[x][y] = {}
    # if z not in dim[x][y]:
        # dim[x][y][z] = '.'
    dim[x][y][z] = val

for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    dim[0][y] = {}
    vals = list(strippedLine)
    for z in range(len(vals)):
        setDim(dim, 0, y, z, vals[z])
    y = y + 1

def isActive(dim, x, y, z):
    return x in dim and y in dim[x] and z in dim[x][y] and dim[x][y][z] == "#"


def countActiveNeighbors(dim, x, y, z):
    neighborCount = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if 0 == i == j == k:
                    continue
                if isActive(dim, x + i, y + j, z + k):
                    neighborCount = neighborCount + 1
    return neighborCount

def countActiveCubes(dim):
    activeCubesCount = 0
    for x in range(xMin, xMax + 1):
        for y in range(yMin, yMax + 1):
            for z in range(zMin, zMax + 1):
                if isActive(dim, x, y, z):
                    # print(str(x) + ", " + str(y) + ", " + str(z))
                    activeCubesCount = activeCubesCount + 1
    return activeCubesCount

def printDims(dim):
    for x in range(xMin, xMax + 1):
        print(x)
        for y in range(yMin, yMax + 1):
            row = ''
            for z in range(zMin, zMax + 1):
                if isActive(dim, x, y, z):
                    row = row + '#'
                else:
                    row = row + '.'
            print(row)

print(dim)
lastConfiguration = dim
print("Active cubes count: " + str(countActiveCubes(lastConfiguration)))
for cycle in range(1, 7):
    nextConfiguration = deepcopy(lastConfiguration)
    for x in range(xMin - 1, xMax + 2):
        for y in range(yMin - 1, yMax + 2):
            for z in range(zMin - 1, zMax + 2):
                activeNeighborsCount = countActiveNeighbors(lastConfiguration, x, y, z)
                if isActive(lastConfiguration, x, y, z):
                    if activeNeighborsCount == 2 or activeNeighborsCount == 3:
                        setDim(nextConfiguration, x, y, z, '#') # stay active, noop
                    else:
                        setDim(nextConfiguration, x, y, z, '.') # deactivate
                else:
                    if activeNeighborsCount == 3:
                        setDim(nextConfiguration, x, y, z, '#') # activate

    lastConfiguration = nextConfiguration
    print("Active cubes count: " + str(countActiveCubes(lastConfiguration)))

# printDims(lastConfiguration)
print("Active cubes count: " + str(countActiveCubes(lastConfiguration)))
