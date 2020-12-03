# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

input = open('input.txt').read().split('\n')

def part1(passwords):
    validPasswords = 0

    for pw in passwords:
        hyphenPos = pw.find('-')  # Int
        firstSpacePos = pw.find(' ')  # Int
        policyLetterPos = pw.find(':') - 1  # Int
        policyLetter = pw[policyLetterPos]  # Str
        testPassword = pw[policyLetterPos + 3:]  # Str

        min = int(pw[:hyphenPos])
        max = int(pw[hyphenPos+1 : firstSpacePos])
        matches = 0  # Matches of policy letter in testPassword

        for char in testPassword:
            if char == policyLetter:
                matches += 1

        if min <= matches <= max:
            validPasswords += 1

    return validPasswords


def part2(passwords):
    validPasswords = 0

    for pw in passwords:
        hyphenPos = pw.find('-')  # Int
        firstSpacePos = pw.find(' ')  # Int
        policyLetterPos = pw.find(':') - 1  # Int
        policyLetter = pw[policyLetterPos]  # Str
        testPassword = pw[policyLetterPos + 3:]  # Str

        position1 = int(pw[:hyphenPos])  # Int
        position2 = int(pw[hyphenPos+1 : firstSpacePos])  # Int

        if policyLetter == testPassword[position1 - 1] or policyLetter == testPassword[position2 - 1]:
            if not (policyLetter == testPassword[position1 - 1] and policyLetter == testPassword[position2 - 1]):
                validPasswords += 1

    return validPasswords


print(part1(input))
print(part2(input))
