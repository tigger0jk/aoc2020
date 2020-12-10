
adapters = []
f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    adapters.append(int(strippedLine))

adapters.sort(reverse=True)
adaptersMap = {}
endJolt = adapters[0]
endNode = {"jolt": endJolt - 3, "chains": {}, "from": {}}
adaptersMap[endJolt] = endNode

def addChainsSpecific(adaptersMap, jolt, toJolt):
    if (toJolt in adaptersMap):
        adaptersMap[toJolt]["chains"][jolt] = jolt
        adaptersMap[jolt]["from"][toJolt] = toJolt

def addChains(adaptersMap, jolt):
    addChainsSpecific(adaptersMap, jolt, jolt + 1)
    addChainsSpecific(adaptersMap, jolt, jolt + 2)
    addChainsSpecific(adaptersMap, jolt, jolt + 3)

for adapter in adapters:
    newNode = {"jolt": adapter, "chains": {}, "from": {}}
    adaptersMap[adapter] = newNode
    addChains(adaptersMap, adapter)

print(adaptersMap)

def multiplyNodes(adaptersMap, node):
    # print(node)
    if ("sum" in node):
        return node["sum"]
    if (len(node["chains"].items()) == 0):
        print("root node")
        node["sum"] = 1
        adaptersMap[node["jolt"]] = node
        return 1
    sum = 0
    for chain in node["chains"]:
        # print(chain)
        sum = sum + multiplyNodes(adaptersMap, adaptersMap[chain])
    if (node["jolt"] - 3 <= 0):
        sum = sum + 1 # straight to root
        print("can reach ground, jolt: " + str(node["jolt"]) + " sum: " + str(sum))
        print(node)
    node["sum"] = sum
    adaptersMap[node["jolt"]] = node
    # print(adaptersMap)
    return sum

print(adaptersMap)

multipliedNodes = multiplyNodes(adaptersMap, adaptersMap[endJolt])
print("answer: " + str(multipliedNodes))
