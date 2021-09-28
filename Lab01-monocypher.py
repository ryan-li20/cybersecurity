def monocypher():
    string = input("Encrypted String")
    letters = {}
    letterAmount = 0
    for x in range(26):
        letters[chr(ord('a') + x)] = 0  # add letters a-z as keys and 0 as init value

    for element in string:
        for letter in letters.keys():
            if element == letter:
                letters.update({element: letters[letter] + 1})
                letterAmount += 1
                break
    for letter in letters:
        letters.update({letter: letters[letter] / letterAmount})

    for x, y in letters.items():  # print out the dictionary in correct format
        print(x, ": ", y)
    print(letterAmount)


monocypher()
