f = open("input.txt", "r")
lineNum = 0
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    if (lineNum == 0):
        targetTime = int(strippedLine)
    if (lineNum == 1):
        times = strippedLine.split(',')

    lineNum = lineNum + 1

print(targetTime)
print(times)
intTimes = []
for time in times:
    if (time == 'x'):
        continue
    intTimes.append(int(time))

print(intTimes)
shortestBusWait = 10000000
bestBusId = -1
for time in intTimes:
    oneBusShort = int(targetTime / time) * time
    if (oneBusShort == targetTime):
        currWait = 0
    else:
        currWait = oneBusShort + time - targetTime
    #  currWait = time - (targetTime % time)
    if (currWait < shortestBusWait):
        bestBusId = time
        shortestBusWait = currWait
        print("new short time: " + str(shortestBusWait))

print("shortest time: " + str(shortestBusWait))
print("best bus: " + str(bestBusId))
# not 37
# not 13 still no
# not 907

print("solution: " + str(bestBusId * shortestBusWait))
