import re

totalValidPasswords = 0

f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    # 1-6 x: dxxxxxx
    res = re.search("(\d*)-(\d*) (\w): (\w*)", strippedLine)
    minCount = int(res.group(1))
    maxCount = int(res.group(2))
    char = res.group(3)
    password = res.group(4)
    print(minCount)
    print(maxCount)
    print(char)
    print(password)

    count = password.count(char)
    if (count <= maxCount and count >= minCount):
        print("valid!")
        totalValidPasswords = totalValidPasswords + 1
    else:
        print("invalid!")

print(totalValidPasswords)

