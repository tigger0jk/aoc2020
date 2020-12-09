WINDOW_SIZE = 25
relevantNumbers = []
relevantMap = {}
allNumbers = []

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

invalidNumber = 0
f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    number = int(strippedLine)
    allNumbers.append(number)
    if (len(relevantNumbers) < WINDOW_SIZE):
        relevantNumbers.append(number)
        addNumberToMap(number, relevantMap)
        continue

    if (not doRelevantNumbersContainSum(relevantMap, number)):
        invalidNumber = number

    #  print(relevantNumbers)
    poppedNum = relevantNumbers.pop(0)
    print("popped num: " + str(poppedNum))
    removeNumberFromMap(poppedNum, relevantMap)
    relevantNumbers.append(number)
    addNumberToMap(number, relevantMap)

print ("INVALID NUMBER: " + str(number))
print ("All numbers count: " + str(len(allNumbers)))

weaknessWindow = []
weaknessSum = 0

i = 0
while(True):
    if weaknessSum < invalidNumber:
        number = allNumbers[i]
        print(number)
        weaknessWindow.append(number)
        weaknessSum = weaknessSum + number
        i = i + 1
    print ("running sum of " + str(len(weaknessWindow)) + " numbers: " + str(weaknessSum))
    if weaknessSum == invalidNumber:
        if len(weaknessWindow) > 1:
            smallestVal = invalidNumber + 1
            largestVal = -1
            for val in weaknessWindow:
                if (val > largestVal):
                    largestVal = val
                if (val < smallestVal):
                    smallestVal = val
            #  firstVal = weaknessWindow[0]
            #  secondVal = weaknessWindow[len(weaknessWindow) - 1]
            print("Weakness window smallest val: " + str(smallestVal))
            print("Weakness window largest val: " + str(largestVal))
            weaknessValue = smallestVal + largestVal
            print ("WEAKNESS VALUE IS: " + str(weaknessValue))
            exit()
    while (weaknessSum > invalidNumber):
        poppedNum = weaknessWindow.pop(0)
        weaknessSum = weaknessSum - poppedNum

print("Not found")
