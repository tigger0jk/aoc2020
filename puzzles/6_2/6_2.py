f = open("input.txt", "r")
totalYesSum = 0
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
groupYesAnswers = {}
for char in alphabet:
    groupYesAnswers[char] = True

for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    if (strippedLine == ''):
        # next group
        currentYes = 0
        for char in alphabet:
            if groupYesAnswers[char]:
                print(char)
                currentYes = currentYes + 1
        totalYesSum = totalYesSum + currentYes
        print("new sum: " + str(totalYesSum))
        groupYesAnswers = {}
        for char in alphabet:
            groupYesAnswers[char] = True
        continue

    for char in alphabet:
        if (char in strippedLine):
            groupYesAnswers[char] = groupYesAnswers[char] and True
        else:
            groupYesAnswers[char] = False

currentYes = 0
for char in alphabet:
    if groupYesAnswers[char]:
        print(char)
        currentYes = currentYes + 1
totalYesSum = totalYesSum + currentYes
print("Total Yes:" + str(totalYesSum))
