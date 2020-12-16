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
validTickets = []
errorScanningRate = 0
for ticket in nearbyTickets:
    validTicket = True
    for value in ticket:
        acceptableFields = []
        # print("for value: " + str(value))
        for fieldName, ranges in rules.items():
            # print("checking ranges: " + str(ranges))
            if (fitsRule(ranges, value)):
                # print("is in range")
                acceptableFields.append(fieldName)
            # else:
                # print("is out of range")
        if(len(acceptableFields) == 0):
            validTicket = False
            errorScanningRate = errorScanningRate + value
    if validTicket:
        validTickets.append(ticket)

print("error scanning rate: " + str(errorScanningRate))
print("valid tickets:")
print(validTickets)
invalidRuleFields = {}
for rule in rules:
    invalidRuleFields[rule] = {}
print (invalidRuleFields)
for ticket in validTickets:
    # for value in ticket:
    for i in range(len(ticket)):
        value = ticket[i]
        for fieldName, ranges in rules.items():
            if (not fitsRule(ranges, value)):
                invalidRuleFields[fieldName][i] = True

print (invalidRuleFields)
fieldMappings = {}
for x in range(200):
    for i in range(len(rules)):
        opts = []
        for fieldName, invalids in invalidRuleFields.items():
            # print(i)
            # print(invalids.keys())
            if i not in invalids.keys():
                opts.append(fieldName)
        # print(opts)
        # if len(opts) == 2:
            # print("2")
            # print(i)
            # print(opts)
        if len(opts) == 1:
            print("field: " + opts[0] + " is it for index: " + str(i))
            fieldMappings[opts[0]] = i
            for fieldName, invalids in invalidRuleFields.items():
                if (fieldName == opts[0]):
                    for i2 in range(len(rules)):
                        invalidRuleFields[fieldName][i2] = True
                # if (fieldName != opts[0]):
                # print("setting invalid for fieldName: " + fieldName + " and i: " + str(i))
                invalidRuleFields[fieldName][i] = True

# print(len(fieldMappings))
# print(len(rules))
print(fieldMappings)
answer = 1
for field, index in fieldMappings.items():
    if "departure" in field:
        answer = answer * myTicket[index]

print("answer:" + str(answer))
