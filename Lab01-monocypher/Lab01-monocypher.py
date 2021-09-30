import math

def part2(string, englishSample):
    base = basecypher(englishSample)  # makes the baseline frequencies
    sd = {}  # string - distance list
    for x in range(1,26):  # makes sd contain the values of all shifted messages : distance from base
        sd[shift(string, x)] = distance(list(cypher(shift(string, x)).values()), list(base.values()))
    sortedsd = sorted(sd.items(), key = lambda kv : kv[1])
    print(sortedsd[0][0])
    
def part1(file):
    base = basecypher(file)  # makes the baseline frequencies
    for x, y in base.items():  # print out the dictionary in correct format
        print(x, ": ", y)
    
    
def shift(string, amount):
    newString = ""
    string = string.lower()
    for char in string:
        if(ord(char) >= ord("a") and ord(char) <= ord("z")):
            newString = newString + (chr((ord(char) - 97 - amount) % 26 + 97))
        else:
            newString = newString + char
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
