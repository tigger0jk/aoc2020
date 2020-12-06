# aoc2020
Advent of Code 2020 https://adventofcode.com/2020

I think the only non-default package I use for the setup is requests
```
pip3 install requests
```

To start a puzzle, run:
```
# get your session token from a request cookie using debug tools on the AOC website
export AOC_SESSION="your session"

python3 createPuzzle.py
```
Do this again once you solve part 1 to start part 2
