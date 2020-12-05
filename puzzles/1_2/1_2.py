
def getComplimentProduct(target):
    array = [None] * (target + 1)
    f = open("input.txt", "r")
    for line in f.readlines():
        num = int(line.strip())
        print(num)
        compliment = target - num
        if (compliment < 0):
            continue
        if (array[compliment]):
            print(str(num) + " and " + str(compliment) + " multiplied is " + str(num*compliment))
            return num*compliment
        array[num] = True
    return None

target = 2020
f = open("input.txt", "r")
for line in f.readlines():
    num = int(line.strip())
    product = getComplimentProduct(target - num)
    if (product != None):
        print(str(num) + " multiplied in is " + str(num*product))
        exit()
