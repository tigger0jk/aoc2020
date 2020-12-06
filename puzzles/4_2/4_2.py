import re

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

def isValidField(value, requiredField):
    if (requiredField == 'byr' or requiredField == 'iyr' or requiredField == 'eyr'):
        if (len(value) != 4):
            return False
        year = int(value)
        minValue = 0
        maxValue = 3000
        if (requiredField == 'byr'):
            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            minValue = 1920
            maxValue = 2002
        if (requiredField == 'iyr'):
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            minValue = 2010
            maxValue = 2020
        if (requiredField == 'eyr'):
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            minValue = 2020
            maxValue = 2030
        if (year < minValue):
            return False
        if (year > maxValue):
            return False
        return True
    if (requiredField == 'hgt'):
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        try:
            height = int(value[:-2])
        except ValueError:
            height = 0
        unit = value[-2:]
        # print("Val:" + value)
        # print("Height: " + height)
        # print("Unit: " + unit)
        if (unit == 'cm'):
            if (height < 150 or height > 193):
                return False
            return True
        elif (unit == 'in'):
            if (height < 59 or height > 76):
                return False
            return True
        else:
            return False
    if (requiredField == 'hcl'):
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        res = re.search("^#[0-9a-f]{6}$", value)
        # print(res)
        if (res == None):
            return False
        return True
    if (requiredField == 'ecl'):
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if (value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            return False
        return True
    if (requiredField == 'pid'):
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        res = re.search("^\d{9}$", value)
        # print(res)
        if (res == None):
            return False
        return True
    return True

validPassports = 0

for passport in passports:
    print(passport)
    missingFields = 0; # this is missing or invalid
    for requiredField in requiredFields:
        if (requiredField not in passport):
            print("missing field: " + requiredField)
            missingFields = missingFields + 1
            continue
        if (not isValidField(passport[requiredField], requiredField)):
            print("missing field: " + requiredField)
            missingFields = missingFields + 1
    if (missingFields == 0):
        validPassports = validPassports + 1

print("Valid Passports: " + str(validPassports))
