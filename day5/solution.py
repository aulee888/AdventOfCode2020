input = open('input.txt').read().split('\n')
sample = open('sample.txt').read().split('\n')

def rowSeat(remainingSeatString, min, max):
    if min == max:
        # Once F and B codes run out, need to figure out column
        return (min, columnSeat(remainingSeatString, 0, 7))

    if remainingSeatString[0] == 'F':
        max = (min + max) // 2
        return rowSeat(remainingSeatString[1:], min, max)

    elif remainingSeatString[0] == 'B':
        min = (min + max) // 2 + 1
        return rowSeat(remainingSeatString[1:], min, max)


def columnSeat(remainingSeatString, min, max):
    if min == max:
        return min

    if remainingSeatString[0] == 'L':
        max = (min + max) // 2
        return columnSeat(remainingSeatString[1:], min, max)

    elif remainingSeatString[0] == 'R':
        min = (min + max) // 2 + 1
        return columnSeat(remainingSeatString[1:], min, max)


def part1(seats):
    highestSeatID = 0
    lowestSeatID = 896

    for codedSeat in seats:
        row, column = rowSeat(codedSeat, 0 , 127)

        if 8 * row + column > highestSeatID:
            highestSeatID = 8 * row + column

        if 8 * row + column < lowestSeatID:
            lowestSeatID = 8 * row + column

    return lowestSeatID, highestSeatID


def part2(takenSeats):
    allSeats = {(i, j): '.' for i in range(128) for j in range(8)}
    lowestSeatID, highestSeatID = part1(takenSeats)

    # Process of eliminaiton -- Full flight. Mark off all taken seats.
    for seat in takenSeats:
        allSeats[rowSeat(seat, 0, 127)] = '#'

    # Below section removes the non-existant seats by using Seat ID
    # Figured out highest possible Seat ID in part 1. Seats don't
    # exist past that Seat ID. Need to figure out lowest Seat ID.
    # Seats don't exist below lowest Seat ID.
    for seat in allSeats:
        currentSeatID = seat[0] * 8 + seat[1]
        if currentSeatID < lowestSeatID or currentSeatID > highestSeatID:
            allSeats[seat] = '#'

    for seat in allSeats:
        if allSeats[seat] == '.':
            return 8 * seat[0] + seat[1]

    return 'No Solution'


print(part1(input))
print(part2(input))
