f = open("input.txt", "r")
startingNums = []
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    for strNum in strippedLine.split(','):
        startingNums.append(int(strNum))
print (startingNums)

i = 0
lastSpakeTimes = {}
lastSaidNum = -1
# targetNum = 2020
targetNum = 30000000
while(i < targetNum):
    if (i < len(startingNums)):
        saidNum = startingNums[i]
    else:
        if (lastSaidNum in lastSpakeTimes):
            saidNum = (i - 1) - lastSpakeTimes[lastSaidNum]
        else:
            saidNum = 0
    print("Turn " + str(i) + " Say: " + str(saidNum))
    lastSpakeTimes[lastSaidNum] = i - 1
    lastSaidNum = saidNum
    i = i + 1
