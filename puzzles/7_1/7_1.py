import re

bags = {}

def ensureBagIsDefined(bagColor):
    if bagColor not in bags:
        bags[bagColor] = {}
        bags[bagColor]["contains"] = []
        bags[bagColor]["contained_in"] = []


f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    #  muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    res = re.search("^([a-zA-Z0-9_\s]*) bags contain( (\d*) ([a-zA-Z0-9_\s]*) bags?[,\.])+$", strippedLine)
    if res == None:
        res = re.search("^([a-zA-Z0-9_\s]*) bags contain no other bags.$", strippedLine)
        if res == None:
            print("NO MATCHES!")
            exit()
        bagColor = res.group(1)
        print(bagColor)
        print("no other bags")
        ensureBagIsDefined(bagColor)
        continue

    bagColor = res.group(1)
    print(bagColor)
    ensureBagIsDefined(bagColor)
    matches = re.findall(" (\d*) ([a-zA-Z0-9_\s]*) bags?[,\.]", strippedLine)
    for match in matches:
        print(match)
        subCount = int(match[0])
        subColor = match[1]
        ensureBagIsDefined(subColor)
        bags[bagColor]["contains"].append(subColor)
        bags[subColor]["contained_in"].append(bagColor)

for bagColor, bag in bags.items():
    print(bagColor + ": " + str(bag))


def countNodes(bagColor):
    if "counted" in bags[bagColor]:
        return 0
    nodeCount = 1
    bags[bagColor]["counted"] = True
    for subColor in bags[bagColor]["contained_in"]:
        nodeCount = nodeCount + countNodes(subColor)
    return nodeCount

MY_BAG_COLOR = "shiny gold"
# now traverse the graph starting at my bag and count all nodes we traverse
nodeCount = countNodes(MY_BAG_COLOR)
nodeCount = nodeCount - 1 # we need to not count our starting node (has to be in SOMETHING)

print("Total bags that could contain mine: " + str(nodeCount))
