
target = 2020

array = [None] * (target + 1)
f = open("input.txt", "r")
for line in f.readlines():
    num = int(line.strip())
    print(num)
    compliment = 2020 - num
    if (array[compliment]):
        print(str(num) + " and " + str(compliment) + " multiplied is " + str(num*compliment))
        exit()
    array[num] = True
