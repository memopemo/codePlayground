# pallete converter from .hex to gamebatte .pal file 
# by Ryan Trozzolo
import sys

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

#create new file
#convert hexadecimal color to color... its so difficult:
#   you gotta take the litteral decimal value of the hexadecimal (:O
#   ...
#   ...
#   THE HORROR. THE PAIN. 
with open(sys.argv[1].replace(".hex", ".pal"), 'w') as f:
    f.write("[General]\n")
    # the order of operations:
    #   take string value of .hex file line
    #   interpret it as a hexadecimal number (base 16)
    #   which is also converted to an int by int("",16)
    #   convert back to a string
    # the rest of the f.write() is just formatting.
    for i in range(0,4):
        f.write("Background" + str(i) + '=' + str(int(lines[i],16)) + "\n")
    for i in range(0,4):
        f.write("Sprite%201" + str(i) + '=' + str(int(lines[i],16)) + "\n")
    for i in range(0,4):
        f.write("Sprite%202" + str(i) + '=' + str(int(lines[i],16)) + "\n")

