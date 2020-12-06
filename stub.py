# import re

f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    # res = re.search("(\d*)-(\d*) (\w): (\w*)", strippedLine)
    # indexOne = int(res.group(1))
