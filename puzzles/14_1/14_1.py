import re

mem = {}
f = open("input.txt", "r")
 # init doesn't matter mask is on the first line
bitmask = 0b0
baseNum = 0b0
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    parts = strippedLine.split(" = ")
    if (parts[0] == 'mask'):
        #  mask = 10XX1100111111100111000010XX00100010
        # convert Xs to 1s and make that a mask
        # replace Xs with 0s and make that a base num
        mask = parts[1]
        bitmaskString = mask.replace('1', '0')
        bitmaskString = bitmaskString.replace('X', '1')
        bitmask = int(bitmaskString, 2)
        baseNumString = mask.replace('X', '0')
        baseNum = int(baseNumString, 2)
        print("string mask:    " + mask)
        print("string bitmask: " + bitmaskString)
        print("string baseNum: " + baseNumString)
        print("bitmask: " + str(bitmask))
        print("baseNum: " + str(baseNum))
    else:
        #  mem[35746] = 6513
        res = re.search("mem\[(\d*)\]", parts[0])
        addr = int(res.group(1))
        value = int(parts[1])
        print("mem addr: " + str(addr))
        print("mem value: " + str(value))
        print("bitmask: " + str(bitmask))
        maskValue = value & bitmask
        print("mask val: " + str(maskValue))
        saveValue = baseNum | maskValue
        print("save val: " + str(saveValue))
        mem[addr] = saveValue
        print("saving: " + str(saveValue))
        # mask the value by ANDing it with the mask
        # take that base num, OR it with the masked value

print(mem)

sum = 0
for addr, val in mem.items():
    sum = sum + val

print("total sum: " + str(sum))
