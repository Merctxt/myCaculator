import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def convertToNumber(string: str):
    newNumber = float(string)

    if newNumber.is_integer():
        newNumber = int(newNumber)
    return newNumber

def isValidNumber(string: str):
    valid = False
    
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

def isEmpty(string: str):
    return len(string) == 0