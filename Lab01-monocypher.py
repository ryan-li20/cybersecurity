import math

def part2(string):
    base = basecypher("aliceInWonderland.txt")  # makes the baseline frequencies
    sd = {}  # string - distance list
    for x in range(26):  # makes sd contain the values of all shifted messages : distance from base
        sd[shift(string, x)] = distance(list(cypher(string).values()), list(base.values()))
    message = ""
    dist = 1
    for x, y in sd.items():  # loops through the frequency, "sorting it", and replacing the message and dist with the better ones
        if(y < dist):
            dist = y
            message = x
            
    print(message)
    
def part1(file):
    base = basecypher(file)  # makes the baseline frequencies
    for x, y in base.items():  # print out the dictionary in correct format
        print(x, ": ", y)
    
    
def shift(string, amount):
    newString = ""
    for char in string:
        print(chr((ord(char) - 97 - amount) % 26 + 97))
        newString = newString + (chr((ord(char) - 97 - amount) % 26 + 97))
    return newString
    
            

def cypher(string):  # returns the list of freq given a string
    based = string.lower()
    letters = {}
    letterAmount = 0
    for x in range(26):
        letters[chr(ord('a') + x)] = 0  # add letters a-z as keys and 0 as init value

    for element in based:
        for letter in letters.keys():
            if element == letter:
                letters.update({element: letters[letter] + 1})
                letterAmount += 1
                break
    for letter in letters:
        letters.update({letter: letters[letter] / letterAmount})
    return letters

def basecypher(file):  # returns the list of freq given a file, establish the baseline
    f = open(file, "r")
    based = f.read().lower()
    letters = {}
    letterAmount = 0
    for x in range(26):
        letters[chr(ord('a') + x)] = 0  # add letters a-z as keys and 0 as init value

    for element in based:
        for letter in letters.keys():
            if element == letter:
                letters.update({element: letters[letter] + 1})
                letterAmount += 1
                break
    for letter in letters:
        letters.update({letter: letters[letter] / letterAmount})
    return letters

def distance(list1, list2):  # given two number lists of equal length, add them together using math, return float
    finalList = []
    finalNumber = 0
    for x in range(len(list1)):
        finalList.append((list1[x] - list2[x]) ** 2)
    for number in finalList:
        finalNumber += number
    return math.sqrt(finalNumber)
