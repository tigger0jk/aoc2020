import re

totalValidPasswords = 0

f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    # 1-6 x: dxxxxxx
    res = re.search("(\d*)-(\d*) (\w): (\w*)", strippedLine)
    indexOne = int(res.group(1))
    indexTwo = int(res.group(2))
    char = res.group(3)
    password = res.group(4)
    print(indexOne)
    print(indexTwo)
    print(char)
    print(password)

    count = password.count(char)
    if ((password[indexOne - 1] == char) != (password[indexTwo - 1] == char)):
        print("valid!")
        totalValidPasswords = totalValidPasswords + 1
    else:
        print("invalid!")

print(totalValidPasswords)

