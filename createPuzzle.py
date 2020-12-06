import os, shutil, urllib.request, requests

AOC_YEAR = '2020'

def makeDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        return True
    return False

puzzle_id = input("Enter puzzle_id (i.e. 3_1):")
puzzle_id = puzzle_id.strip()
parts = puzzle_id.split('_')
day = int(parts[0])
part = int(parts[1])
print("Day " + str(day) + " - Part " + str(part))

PUZZLES_DIR = 'puzzles'
makeDir(PUZZLES_DIR)

part1Id = str(day) + '_1'
part2Id = str(day) + '_2'

part1Dir = os.path.join(PUZZLES_DIR, part1Id)
part2Dir = os.path.join(PUZZLES_DIR, part2Id)

part1ScriptPath = os.path.join(part1Dir, part1Id + '.py')
part2ScriptPath = os.path.join(part2Dir, part2Id + '.py')

part1InputPath = os.path.join(part1Dir, 'input.txt')
part2InputPath = os.path.join(part2Dir, 'input.txt')

if (part == 1):
    # print("part 1")
    fileWasCreated = makeDir(part1Dir)
    if(not fileWasCreated):
        prompt = input(part1Dir + " already exists, are you sure you want to clobber it? 'yes' to continue, anything else to stop: ")
        if (prompt != "yes"):
            exit()
    shutil.copyfile('stub.py', part1ScriptPath)
    SESSION_ENV_VAR = 'AOC_SESSION'
    try:
        session = os.environ[SESSION_ENV_VAR]
    except KeyError:
        print("Please export your session id from console into " + SESSION_ENV_VAR)
        exit()
    print("SESSION: " + session)

    cookies = {'session': session}
    inputUrl = "https://adventofcode.com/" + AOC_YEAR + "/day/" + str(day) + "/input"
    # print(inputUrl)
    # print(part1InputPath)

    r = requests.get(inputUrl, cookies=cookies)
    with open(part1InputPath, 'wb') as f:
        f.write(r.content)
    lines = r.text.split('\n')
    targetLineCount = 3
    if (len(lines) < targetLineCount):
        print("Full Input (less than " + str(targetLineCount) + " lines, maybe ERROR!):")
        print(r.text)
    else:
        print("First " + str(targetLineCount) + " lines of input:")
        for lineIndex in range(targetLineCount):
            print(lines[lineIndex])
        # print(r.text[0:newLinePos])
    print("Created: " + part1Dir)
elif (part == 2):
    # print("part 2")
    fileWasCreated = makeDir(part2Dir)
    if(not fileWasCreated):
        prompt = input(part2Dir + " already exists, are you sure you want to clobber it? 'yes' to continue, anything else to stop: ")
        if (prompt != "yes"):
            exit()
    shutil.copyfile(part1ScriptPath, part2ScriptPath)
    shutil.copyfile(part1InputPath, part2InputPath)
    print("Created: " + part2Dir)
