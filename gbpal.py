# pallete converter from .hex to gamebatte .pal file 
# useful for creating pallete files for use with RetroArch's Gamebatte core or the standalone emulator. 
#
#   USAGE = py gbpal.py [file]
#
# Works with:
#   Gimp Palettes (.gpl)
#   Paint.NET Palettes (.txt)
#   JASC Palettes (.pal)
#   Hexadecimal Palletes (.hex)
#   Gamebatte Palletes (.pal) (idiot proofing)
# 
# IMPORTANT FORMAT INFO:
# COLOR ORDER MUST BE: 
#   White
#   Light
#   Dark
#   Black
#
# USE 'gbpalreverser.py' TO REVERSE COLOR ON CONVERTED .PAL FILE IF NECESSARY
# 
# by Ryan Trozzolo
import sys

if(len(sys.argv) == 1):
    colors = [0,0,0,0]
    colors[0] = str(int(input("Enter White Hexadecimal:"),16))
    colors[1] = str(int(input("Enter Light Hexadecimal:"),16))
    colors[2] = str(int(input("Enter Dark Hexadecimal:"),16))
    colors[3]= str(int(input("Enter Black Hexadecimal:"),16))
    output = input("Enter name of palette (.pal will be added on end)")
    with open(output+'.pal','w') as f:
        f.write("[General]\n")
        def writewith(x):
            for index, item in enumerate(colors):
                f.write(f"{x}{index}={item}\n")
        writewith("Background")
        writewith("Sprite%201")
        writewith("Sprite%202")
        print(f"Sucessfully completed: Created {output}.pal")
    input()
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

#branch on file type, yes it does this every time
def determineType(index: int) -> int:
    if(lines[0] == "GIMP Palette"):
        print("Converting GIMP file color #" + str(index + 1))
        return GPLtoPAL(index)
    elif(lines[0] == ";paint.net Palette File"):
        print("Converting Paint.Net file color #" + str(index + 1))
        return PDNtoPAL(index)
    elif(lines[0] == "JASC-PAL"):
        print("Converting JASC file color #" + str(index + 1))
        return JASCtoPAL(index)
    elif(lines[0] == "[General]"):
        exit("Already a .pal file")
    else:
        print("Converting HEX file color #" + str(index + 1))
        return HEXtoPAL(index)
# Contains Hexadecimal on the 4th word
def GPLtoPAL(index: int):
    return int(lines[4 + index].split()[3],16)
# Needs to trim off the FF transparency value
def PDNtoPAL(index: int):
    return int(lines[5 + index],16) & 0x00FFFFFF  #remove pesky transparency value

# Convert 3 RGB numbers to one decimal number
def JASCtoPAL(index: int):
    def getNumber(i: int):
        return int(lines[3 + index].split()[i])
    return (getNumber(0)*256*256)+(getNumber(1)*256)+getNumber(2)

# int supports strings formatted as hex
def HEXtoPAL(index: int):
    return int(lines[i],16)

#idiot proofing
def PALtoPAL(index:int):
    return int((lines[index+1].removeprefix("Background" + str(index) + '=')))

#TODO: add support for finding the palettes in image files (.png, .jpg?, .bmp) using PIL's Image


# convert given hexadecimal to pal
with open(sys.argv[1] + ".pal", 'w') as f:
    f.write("[General]\n")
    def writewith(x):
        for i in range(0,4):
            f.write(f"{x}{i}={determineType(i)}\n")
    writewith("Background")
    writewith("Sprite%201")
    writewith("Sprite%202")
    exit(f"Sucessfully completed: Created {sys.argv[1]}.pal")

