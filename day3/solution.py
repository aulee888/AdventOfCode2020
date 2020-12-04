input = open('input.txt').read().split('\n')
sample = open('sample.txt').read().split('\n')

def part1(geoMap):
    treesEncountered = 0
    mapWidth = len(geoMap[0])
    xPosition = 0

    for row in geoMap[1:]:  # Don't consider 1st row b/c it moves right 3, down 1
        xPosition = (xPosition + 3) % mapWidth

        if row[xPosition] == '#':
            treesEncountered += 1

    return treesEncountered


def part2(geoMap):
    treesEncounteredMultiplier = []
    mapWidth = len(geoMap[0])
    mapLength = len(geoMap)
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    for slope in slopes:
        treesEncountered = 0
        xPosition = 0
        yPosition = 0

        while yPosition < mapLength - 1:
            xPosition = (xPosition + slope[0]) % mapWidth
            yPosition += slope[1]
            # print(xPosition, yPosition)

            # if yPosition > mapLength - 1:
            #     break

            if geoMap[yPosition][xPosition] == '#':
                treesEncountered += 1
        
        treesEncounteredMultiplier.append(treesEncountered)

    print(treesEncounteredMultiplier)
    result = 1
    for i in treesEncounteredMultiplier:
        result *= i

    return result

# print(part1(input))
print(part2(input))