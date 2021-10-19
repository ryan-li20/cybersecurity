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
    count = 0
    for char in inp:
        xor(char, key[count])
        
def xor(l1,l2):
    num1 = ord(l1)
    num2 = ord(l2)
    return num1 ^ num2
