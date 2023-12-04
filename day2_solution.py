import re
file = open("day2_input.txt")
totalCubes = {"red": 12, "green": 13, "blue": 14}
result = 0
gameNumber = 0
for line in file.readlines():
    line = line.strip()
    gameData = line.split(': ')
    gameSets = gameData[1].split("; ")
    resultGame = True
    gameNumber += 1

    for sets in gameSets:
        splitSet = sets.split(', ')
        for numColors in splitSet:
            numsAndColors = numColors.split(' ')
            if (int(numsAndColors[0]) > totalCubes[numsAndColors[1]]):
                resultGame = False
            print(numsAndColors)
    print("New Game")
    print(resultGame)
    if resultGame:
        result += gameNumber
print(result)

