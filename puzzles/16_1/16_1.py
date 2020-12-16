import re

def parseTicket(line):
    ticket = []
    for value in strippedLine.split(','):
        ticket.append(int(value))
    return ticket

f = open("input.txt", "r")
parsingMode = 0
rules = {}
myTicket = None
nearbyTickets = []
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    if len(strippedLine) == 0:
        parsingMode = parsingMode + 1
        continue
    if parsingMode == 0:
        # arrival platform: 26-89 or 105-970
        print("parsing rules")
        res = re.search("^([a-zA-Z0-9_ ]*): (\d*)-(\d*) or (\d*)-(\d*)$", strippedLine)
        fieldName = res.group(1)
        firstMin = int(res.group(2))
        firstMax = int(res.group(3))
        secondMin = int(res.group(4))
        secondMax = int(res.group(5))
        print(fieldName)
        print(firstMin)
        print(firstMax)
        print(secondMin)
        print(secondMax)
        rules[fieldName] = [firstMin, firstMax, secondMin, secondMax]
    elif parsingMode == 1:
        print("parsing my ticket")
        if "ticket" in strippedLine:
            continue
        myTicket = parseTicket(strippedLine)
    elif parsingMode == 2:
        print("parsing nearby tickets")
        # 135,496,574,158,132,495,859,588,863,148,243,742,329,824,315,786,659,300,716,160
        if "ticket" in strippedLine:
            continue
        nearbyTickets.append(parseTicket(strippedLine))

def fitsRule(ranges, value):
    return ranges[0] <= value <= ranges[1] or ranges[2] <= value <= ranges[3]

print (nearbyTickets)
errorScanningRate = 0
for ticket in nearbyTickets:
    for value in ticket:
        acceptableFields = []
        print("for value: " + str(value))
        for fieldName, ranges in rules.items():
            print("checking ranges: " + str(ranges))
            if (fitsRule(ranges, value)):
                print("is in range")
                acceptableFields.append(fieldName)
            else:
                print("is out of range")
        if(len(acceptableFields) == 0):
            errorScanningRate = errorScanningRate + value

print("error scanning rate: " + str(errorScanningRate))
