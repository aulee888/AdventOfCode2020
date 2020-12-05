sample = open('sample.txt').read().split('\n\n')
input = open('input.txt').read().split('\n\n')

# Clean up each passport so that each field is an item of list.
# First replace any line breaks with a space.
# Then separate each field based on space as separator.
cleanSample = []
for passport in sample:
    cleanSample.append(passport.replace('\n', ' ').split(' '))

cleanInput = []
for passport in input:
    cleanInput.append(passport.replace('\n', ' ').split(' '))

def haveAllFields(passportBatch: list):
    # passportBatch is a list of list of fields
    reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optField = 'cid'
    validPassports = []

    for passport in passportBatch:
        valid = 0
        cid = False

        for field in reqFields:
            # Checks if reqField is contained in the passport by iterating
            # through each listed info on passport.
            for info in passport:
                if optField == info[:3]:
                    cid = True
                
                if field == info[:3]:
                    valid += 1
                    break
                
        if valid == len(reqFields):
            validPassports.append(passport)

    return validPassports


def birthYear(year: str):
    if len(year) == 4 and 1920 <= int(year) <= 2002:
        return True
    else:
        return False


def issueYear(year: str):
    if len(year) == 4 and 2010 <= int(year) <= 2020:
        return True
    else:
        return False


def expirationYear(year: str):
    if len(year) == 4 and 2020 <= int(year) <= 2030:
        return True
    else:
        return False


def height(hgt: str):
    if hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            return True
        else:
            return False
            
    elif hgt[-2:] == 'cm':
        if 150 <= int(hgt[:-2]) <= 193:
            return True
        else:
            return False

    else:
        # print(f"'{hgt}' is not a valid value!")
        return False


def hairColor(color: str):
    reqChar = '0123456789abcdef'
    validHairColor = True

    if color[0] != '#':
        validHairColor = False

    for symbol in color[1:]:
        if symbol not in reqChar:
            validHairColor = False

    return validHairColor


def eyeColor(color: str):
    reqColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if color in reqColors:
        return True
    else:
        return False


def passportID(id: str):
    if len(id) == 9:
        return True
    else:
        return False


def countryID(id: str):
    return True


valueTest = {
    'byr': birthYear,
    'iyr': issueYear,
    'eyr': expirationYear,
    'hgt': height,
    'hcl': hairColor,
    'ecl': eyeColor,
    'pid': passportID,
    'cid': countryID
}

def haveValidValues(passportBatch):
    validPassports = []

    for passport in passportBatch:
        validInfo = True

        for field in passport:
            key = field[:3]
            listedInfo = field[4:]
            
            if not valueTest[key](listedInfo):
                validInfo = False
                break
        
        if validInfo:
            validPassports.append(passport)

    return validPassports
        


def part1(passportBatch):
    return len(haveAllFields(passportBatch))


def part2(passportBatch):
    return len(haveValidValues(passportBatch))

print(part1(cleanInput))
print(part2(haveAllFields(cleanInput)))
