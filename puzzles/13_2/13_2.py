import math

f = open("input.txt", "r")
#  f = open("exampleInput.txt", "r")
lineNum = 0
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    if (lineNum == 0):
        targetTime = int(strippedLine)
    if (lineNum == 1):
        times = strippedLine.split(',')

    lineNum = lineNum + 1

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

allLcms = {}
def lcms(targetTimes):
    key = len(targetTimes)
    if (key in allLcms) :
        return allLcms[key]
    runningLcm = targetTimes[0][0]
    for i in range(1, len(targetTimes)):
        runningLcm = lcm(runningLcm, targetTimes[i][0])
    allLcms[key] = runningLcm
    return runningLcm

print(targetTime)
print(times)
targetTimes = []
departOffset = -1
for time in times:
    departOffset = departOffset + 1
    if (time == 'x'):
        continue
    targetTimes.append([int(time), departOffset])

firstBusTime = targetTimes[0][0]
print(targetTimes)
departTime = 0
while(True):
    #  print(departTime)
    foundIt = True
    for i in range(len(targetTimes)):
        time = targetTimes[i]
        if ((departTime + time[1]) % time[0] != 0):
            foundIt = False
            break

    if(foundIt):
        print("target time is " + str(departTime))
        exit()
    departTime = departTime + lcms(targetTimes[0:i])

