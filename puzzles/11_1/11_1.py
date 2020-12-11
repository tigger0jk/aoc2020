from copy import copy, deepcopy

seats = []

f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    row = []
    for char in strippedLine:
        row.append(char)
    seats.append(row)

def configsIdentical(config1, config2):
    for rowId, row in enumerate(config1):
        for valId, val in enumerate(row):
            if (val != config2[rowId][valId]):
                return False
    return True

def isOccupied(config, rowId, valId):
    if (rowId < 0 or rowId >= len(config)):
        return False
    if (valId < 0 or valId >= len(config[0])):
        return False
    return config[rowId][valId] == "#"

def countAdjacents(config, rowId, valId):
    adjacents = 0
    adjacents = adjacents + isOccupied(config, rowId - 1, valId - 1)
    adjacents = adjacents + isOccupied(config, rowId - 1, valId + 0)
    adjacents = adjacents + isOccupied(config, rowId - 1, valId + 1)
    adjacents = adjacents + isOccupied(config, rowId + 0, valId - 1)
    adjacents = adjacents + isOccupied(config, rowId + 0, valId + 1)
    adjacents = adjacents + isOccupied(config, rowId + 1, valId - 1)
    adjacents = adjacents + isOccupied(config, rowId + 1, valId + 0)
    adjacents = adjacents + isOccupied(config, rowId + 1, valId + 1)
    return adjacents

lastConfiguration = seats
steps = 0
while(True):
    nextConfiguration = deepcopy(lastConfiguration)

    for rowId, row in enumerate(lastConfiguration):
        for valId, val in enumerate(row):
            if (val == '.'):
                continue
            adjacents = countAdjacents(lastConfiguration, rowId, valId)
            #  print("adjacents: " + str(adjacents))
            if (val == 'L' and adjacents == 0):
                nextConfiguration[rowId][valId] = '#'
            elif (val == '#' and adjacents >= 4):
                nextConfiguration[rowId][valId] = 'L'

    steps = steps + 1
    print ("Steps: " + str(steps))
    if (configsIdentical(lastConfiguration, nextConfiguration)):
        break
    lastConfiguration = nextConfiguration

print("Final config: ")
print(lastConfiguration)

takenSeats = 0
for rowId, row in enumerate(lastConfiguration):
    for valId, val in enumerate(row):
        if (val == '#'):
            takenSeats = takenSeats + 1


print("Taken seats: " + str(takenSeats))
