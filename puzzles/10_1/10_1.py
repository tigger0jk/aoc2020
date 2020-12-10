
adapters = []
# f = open("exampleInput1.txt", "r")
f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    adapters.append(int(strippedLine))

adapters.sort()
prevAdapter = 0
oneDiffs = 0
threeDiffs = 1

for adapter in adapters:
    diff = adapter - prevAdapter
    if (diff > 3):
        print("ERROR - DIFF OVER 3: " + str(diff))
        print (str(prevAdapter))
        print (str(adapter))
        exit()
    if (diff == 1):
        oneDiffs = oneDiffs + 1
    if (diff == 3):
        threeDiffs = threeDiffs + 1
    print(str(adapter))
    prevAdapter = adapter

print ("oneDiffs: " + str(oneDiffs))
print ("threeDiffs: " + str(threeDiffs))
print ("answer: " + str(oneDiffs * threeDiffs))
