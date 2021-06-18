from decimal import *
from BigNumber import *

newNumber = ""

# dictionaries for character value
# for values above 9, they are associated with a letter
# these are used in notation for base 10+
toDecimalDict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35 
}

toAnyDict = {
    0: '0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F',
    16:'G',
    17:'H',
    18:'I',
    19:'J',
    20:'K',
    21:'L',
    22:'M',
    23:'N',
    24:'O',
    25:'P',
    26:'Q',
    27:'R',
    28:'S',
    29:'T',
    30:'U',
    31:'V',
    32:'W',
    33:'X',
    34:'Y',
    35:'Z'
}

# functions
# if the decimal value of input is larger than 15 digits, this will break down
def convert(inputNumber, fromBase, toBase):
    # currently only doing whole integers
    # no validations yet

    newNumber = ""

    if "." in inputNumber:
        inputArr = inputNumber.split(".")
        integral = inputArr[0]
        fractional = inputArr[1]
    else:
        integral = inputNumber
        fractional = ""

    sum = 0
    position = 0 # track position for exponent
    for character in reversed(integral): # loops through the reversed string
        value = toDecimalDict[character]
        sum += value * (fromBase ** position)
        position += 1

    newIntegral = ""
    while sum > 0:
        remainder = sum % toBase
        character = toAnyDict[remainder]
        newNumber = str(character) + newNumber
        sum = int(sum / toBase)
    # integral conversion is accurate up to 21 and including decimal digits



    if fractional != "":
        newNumber += "."
        #convert to decimal
        sum = 0
        index = 0
        for char in fractional:
            getcontext().prec = index + 20
            position = (index * -1) -1
            value = toDecimalDict[char]
            sum += value * Decimal(fromBase ** position)
            index += 1

        # convert to new
        count = 0
        while sum > 0 and count < 30:
            getcontext().prec = 30
            holdIntegral = int(sum * toBase)
            char = toAnyDict[holdIntegral]
            newNumber += char
            sum = sum * toBase - holdIntegral
            count += 1
        # fractional has variable accuracy so far
        # anywhere from 8 to 20 digits


    return newNumber





# originalBase input loop
while True:
    userInput = input("Please enter a base to convert from: ")

    # check for parsable input
    try:
        fromBase = int(userInput)
    except:
        print("Please enter a whole integer (2-36).")
        continue

    # if outside of the range of conversion
    if fromBase < 2 or fromBase > 36:
        print("Please enter a whole integer (2-36).")
        continue
    
    break

# toBase input loop
while True:
    userInput = input("Please enter a base to convert to: ")

    # check for parsable input
    try:
        toBase = int(userInput)
    except:
        print("Please enter a whole integer (2-36).")
        continue

    # make sure in range of conversion
    if toBase < 2 or toBase > 36:
        print("Please enter a whole integer (2-36).")
        continue

    # check if same as fromBase
    if toBase == fromBase:
        print("Please don't use the same base for both.")
        continue
    break

# number input loop, still need to verify correct notation
while True:
    userInput = input("Please enter a number using correct base notation: ")

    hasPoint = False
    repeat = False
    
    # still need to validate correct notation
    for char in userInput:
        if char == "." and hasPoint == False:
            # ignore floating points
            hasPoint = True
            continue
        elif char == "." and hasPoint == True:
            # don't ignore multiple floating points
            print("Do not use multiple points.")
            repeat = True
            break
        elif fromBase <= toDecimalDict[char]:
            # checks value associated with character. Cannot be equal or greater than base converting from
            print("Please use correct notation for the base you're converting from (refer to README if need be).")
            repeat = True
            break

    if repeat == True:
        continue    

    break




newNumber = convert(userInput, fromBase, toBase) # returns string
print(userInput + " --> " + newNumber)
input("press enter to leave")


