f = open("input.txt", "r")
totalYesSum = 0
groupYesAnswers = {}
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    if (strippedLine == ''):
        # next group
        totalYesSum = totalYesSum + len(groupYesAnswers.keys())
        print("new sum: " + str(totalYesSum))
        groupYesAnswers = {}

    for char in strippedLine:
        groupYesAnswers[char] = True

totalYesSum = totalYesSum + len(groupYesAnswers.keys())
print("Total Yes:" + str(totalYesSum))
