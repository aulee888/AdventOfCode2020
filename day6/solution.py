input = open('input.txt').read().split('\n\n')
sample = open('sample.txt').read().split('\n\n')


# Clean up each passport so that each field is an item of list.
# First replace any line breaks with a space.
# Then separate each field based on space as separator.
cleanSample = []
for group in sample:
    cleanSample.append(group.replace('\n', ' ').split(' '))

cleanInput = []
for group in input:
    cleanInput.append(group.replace('\n', ' ').split(' '))


def part1(passengerGroups):
    questionsString = 'abcdefghijklmnopqrstuvwxyz'
    totalQuestions = 0

    for group in passengerGroups:
        groupAnswerSheet = {letter: '.' for letter in questionsString}

        for person in group:
            
            for answeredQ in person:
                if groupAnswerSheet[answeredQ] == '.':
                    groupAnswerSheet[answeredQ] = '#'

        for markedQ in groupAnswerSheet:
            if groupAnswerSheet[markedQ] == '#':
                totalQuestions += 1
    
    return totalQuestions


def part2(passengerGroups):
    questionString = 'abcdefghijklmnopqrstuvwxyz'
    totalQuestions = 0
    
    for group in passengerGroups:
        groupAnswerSheet = {letter: 0 for letter in questionString}

        for person in group:

            for answeredQ in person:
                groupAnswerSheet[answeredQ] += 1

        for letter in questionString:
            if groupAnswerSheet[letter] == len(group):
                totalQuestions += 1

    return totalQuestions


print(part1(cleanInput))
print(part2(cleanInput))