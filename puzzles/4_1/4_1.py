passports = []
currentPassport = None

f = open("input.txt", "r")
for line in f.readlines():
    if (currentPassport == None):
        currentPassport = {}

    strippedLine = line.strip()
    print(strippedLine)

    if (strippedLine == ''):
        passports.append(currentPassport)
        currentPassport = None
    else:
        elements = strippedLine.split(' ')
        for element in elements:
            parts = element.split(':')
            currentPassport[parts[0]] = parts[1]

if (currentPassport != None):
    passports.append(currentPassport)

requiredFields = [
        'byr', # (Birth Year)
        'iyr', # (Issue Year)
        'eyr', # (Expiration Year)
        'hgt', # (Height)
        'hcl', # (Hair Color)
        'ecl', # (Eye Color)
        'pid', # (Passport ID)
        # 'cid', # (Country ID)
        ]

validPassports = 0

for passport in passports:
    print(passport)
    missingFields = 0;
    for requiredField in requiredFields:
        if (requiredField not in passport):
            print("missing field: " + requiredField)
            missingFields = missingFields + 1
    if (missingFields == 0):
        validPassports = validPassports + 1

print("Valid Passports: " + str(validPassports))
