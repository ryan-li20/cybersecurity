import math
import sys;




def factorize(number):
    lis = []
    print(type(number))
    for x in range(2,int(number/2)):
        while number % x == 0:
            lis.append(x)
            number /= x
    print(lis)
    
def buckets(string):
    lis1 = []
    lis2 = []
    lis3 = []
    lis4 = []
    for x in range(len(string)):
        if x % 4 == 0:
            lis1.append(string[x])
        if x % 4 == 1:
            lis2.append(string[x])
        if x % 4 == 2:
            lis3.append(string[x])
        if x % 4 == 3:
            lis4.append(string[x])
    return[lis1, lis2, lis3, lis4]
    
def unbucket(string1, string2, string3, string4):
    string = ""
    for x in range(len(string2)): #  FIX THIS PART, EACH INDIVIDUAL WITH A IF STATEMENT BEFORE IT TO CHECK UNDONENESS
        string = string + string1[x] + string2[x] + string3[x] + string4[x]
    print(string)

def stringify(lis):
    string = "".join(lis)
    return string

def part2(string, englishSample):
    base = basecypher(englishSample)  # makes the baseline frequencies
    sd = {}  # string - distance list
    for x in range(1,26):  # makes sd contain the values of all shifted messages : distance from base
        sd[shift(string, x)] = distance(list(cypher(shift(string, x)).values()), list(base.values()))
    sortedsd = sorted(sd.items(), key = lambda kv : kv[1])
    return(sortedsd[0][0])
    
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

def decode(string):
    unbucket(     part2(stringify(buckets(string)[0]), "aliceInWonderland.txt")    , part2(stringify(buckets(string)[1]), "aliceInWonderland.txt"),     part2(stringify(buckets(string)[2]), "aliceInWonderland.txt"),      part2(stringify(buckets(string)[3])  , "aliceInWonderland.txt")           )


