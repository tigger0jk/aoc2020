WINDOW_SIZE = 25
relevantNumbers = []
relevantMap = {}

def addNumberToMap(number, map):
    if (number in map.keys()):
        map[number] = map[number] + 1
        return
    map[number] = 1

def removeNumberFromMap(number, map):
    if (number in map.keys()):
        if (map[number] > 1):
            map[number] = map[number] - 1
            return
        del map[number]
        return
    raise

def doRelevantNumbersContainSum(map, sum):
    for number, count in map.items():
        if count > 1 and number + number == sum:
            return True
        otherNumber = sum - number
        if otherNumber in map.keys():
            return True
    return False

f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    number = int(strippedLine)
    if (len(relevantNumbers) < WINDOW_SIZE):
        relevantNumbers.append(number)
        addNumberToMap(number, relevantMap)
        continue

    if (not doRelevantNumbersContainSum(relevantMap, number)):
        print ("INVALID NUMBER: " + str(number))
        exit()

    #  print(relevantNumbers)
    poppedNum = relevantNumbers.pop(0)
    print("popped num: " + str(poppedNum))
    removeNumberFromMap(poppedNum, relevantMap)
    relevantNumbers.append(number)
    addNumberToMap(number, relevantMap)

