#reverses palletes if they were imported in the opposite order :)

import sys

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

with open("rv."+sys.argv[1], 'w') as f:
    f.write("[General]\n")
    
    f.write("Background0=" + lines[4].removeprefix("Background3=")+"\n")
    f.write("Background1=" + lines[3].removeprefix("Background2=")+"\n")
    f.write("Background2=" + lines[2].removeprefix("Background1=")+"\n")
    f.write("Background3=" + lines[1].removeprefix("Background0=")+"\n")

    f.write("Sprite%2010=" + lines[8].removeprefix("Sprite%2013=")+"\n")
    f.write("Sprite%2011=" + lines[7].removeprefix("Sprite%2012=")+"\n")
    f.write("Sprite%2012=" + lines[6].removeprefix("Sprite%2011=")+"\n")
    f.write("Sprite%2013=" + lines[5].removeprefix("Sprite%2010=")+"\n")

    f.write("Sprite%2020=" + lines[12].removeprefix("Sprite%2023=")+"\n")
    f.write("Sprite%2021=" + lines[11].removeprefix("Sprite%2022=")+"\n")
    f.write("Sprite%2022=" + lines[10].removeprefix("Sprite%2021=")+"\n")
    f.write("Sprite%2023=" + lines[9].removeprefix("Sprite%2020=")+"\n")

