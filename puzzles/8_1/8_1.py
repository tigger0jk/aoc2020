import re

def createInstruction(instruction, sign, value):
    if (sign == "-"):
        value = -value
    return {"instruction": instruction, "value": value}

instructions = []
f = open("input.txt", "r")
for line in f.readlines():
    strippedLine = line.strip()
    print(strippedLine)
    res = re.search("(\w*) ([+-])(\d*)", strippedLine)
    instruction = res.group(1)
    print(instruction)
    sign = res.group(2)
    print(sign)
    value = int(res.group(3))
    print(value)
    instructions.append(createInstruction(instruction, sign, value))

visitedInstructions = {}
acc = 0
instructionIndex = 0
while (True):
    instruction = instructions[instructionIndex]
    print(str(instructionIndex) + ": " + str(instruction))
    if instructionIndex in visitedInstructions:
        break
    visitedInstructions[instructionIndex] = True
    if instruction['instruction'] == "acc":
        acc = acc + instruction['value']
        print("new acc: " + str(acc))
        instructionIndex = instructionIndex + 1
    if instruction['instruction'] == "nop":
        instructionIndex = instructionIndex + 1
    if instruction['instruction'] == "jmp":
        instructionIndex = instructionIndex + instruction['value']

print("acc was: " + str(acc))
