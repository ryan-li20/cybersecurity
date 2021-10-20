import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile,"rb").read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
  print("mode:"+mode)
  print("key: "+key)
  print("inp: "+inp)



def human(inp, key):
    while len(inp) > len(key):
        key = key + key
    output = ""
    count = 0
    for char in inp:
        output = output + chr(xor(char, key[count]))
    f = open("output.txt", "a")
    f.write(output)
    return output
        
def xor(l1,l2): # given two characters, return the decimal value of them xored
    num1 = ord(l1)
    num2 = ord(l2)
    return num1 ^ num2

def integerout(inp, key):
    while len(inp) > len(key):
        key = key + key
    output = ""
    count = 0
    for char in inp:
        tmp = "" + hex(xor(char, key[count]))
        output = output + tmp[2:] + " "
    print(output)
    return output

if(mode == "numOut"):
    integerout(inp, key)
if(mode == "human"):
    human(inp, key)