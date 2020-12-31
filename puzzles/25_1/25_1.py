# f = open("exampleInput.txt", "r")
f = open("input.txt", "r")
cardPublicKey = 0
doorPublicKey = 0
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    if cardPublicKey == 0:
        cardPublicKey = int(strippedLine)
    else:
        doorPublicKey = int(strippedLine)

print(cardPublicKey)
print(doorPublicKey)

subjectNumber = 7
loopCount = 0
cardLoopSize = 0
doorLoopSize = 0
value = 1
while(doorLoopSize == 0 or cardLoopSize == 0):
    if value == cardPublicKey:
        # print("FOUND CARD: " + str(loopCount))
        cardLoopSize = loopCount
    if value == doorPublicKey:
        # print("FOUND DOOR: " + str(loopCount))
        doorLoopSize = loopCount
    loopCount = loopCount + 1
    value = value * subjectNumber
    value = value % 20201227
    # print(value)

print("card loop size: "+ str(cardLoopSize)) # 15260454
print("door loop size: "+ str(doorLoopSize)) # 10476062

def transform(subjectNumber, loopSize):
    value = 1
    for i in range(loopSize):
        value = value * subjectNumber
        value = value % 20201227
    return value

encryptionKeyFromCard = transform(doorPublicKey, cardLoopSize)
print("encryptionKeyFromCard: " + str(encryptionKeyFromCard)) # 448851
# encryptionKeyFromDoor = transform(cardPublicKey, doorLoopSize)
# print("encryptionKeyFromDoor: " + str(encryptionKeyFromDoor)) # 448851
