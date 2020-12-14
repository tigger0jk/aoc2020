import re

def generateBitmaskPermutations(bitmask):
    perms = [0b0]
    bitCheck = 0b1
    while (bitCheck <= 0b100000000000000000000000000000000000):
        posVal = bitCheck & bitmask
        if (posVal != 0):
            # there's a 1 at this digit, try both
            newPerms = []
            for perm in perms:
                newPerms.append(perm | bitCheck)
            perms.extend(newPerms)
            print(perms)
        bitCheck = bitCheck << 1

    return perms

mem = {}
#  f = open("exampleInput.txt", "r")
f = open("input.txt", "r")
 # init doesn't matter mask is on the first line
bitmask = 0b0
baseNum = 0b0
bitmaskPerms = []
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    parts = strippedLine.split(" = ")
    if (parts[0] == 'mask'):
        mask = parts[1]
        bitmaskString = mask.replace('1', '0')
        bitmaskString = bitmaskString.replace('X', '1')
        bitmask = int(bitmaskString, 2)
        inverseBitmask = ~bitmask
        baseNumString = mask.replace('X', '0')
        baseNum = int(baseNumString, 2)
        bitmaskPerms = generateBitmaskPermutations(bitmask)
        print("string mask:    " + mask)
        print("string bitmask: " + bitmaskString)
        print("string baseNum: " + baseNumString)
        print("bitmask: " + str(bitmask))
        print("baseNum: " + str(baseNum))
    else:
        res = re.search("mem\[(\d*)\]", parts[0])
        addr = int(res.group(1))
        value = int(parts[1])
        newAddr = addr & inverseBitmask
        newAddr = baseNum | newAddr
        for bitmaskPerm in bitmaskPerms:
            finalAddr = newAddr | bitmaskPerm
            #  print("final addr: " + str(finalAddr))
            mem[finalAddr] = value

print(mem)

sum = 0
for addr, val in mem.items():
    sum = sum + val

print("total sum: " + str(sum))
