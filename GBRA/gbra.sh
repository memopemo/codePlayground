#!/bin/bash
#Find every file in locations given in dirs.txt, create it if it doesnt exist.
#find latest file (using -nt)
#rsync latest file to other file locations

if [ ! $1 ] 
then
    echo "usage: gbra.sh [file]"
    exit 1
fi

if [ ! -f dirs.txt ]; then
    echo "Creating dirs.txt with '.' in current directory. Add your Save Folders to be updated to this file."
    echo "." > dirs.txt
fi

mapfile -t dirArray < dirs.txt

allSavs=()

#find each save file that exists.
for i in ${dirArray[@]} 
do
    if [[ -f "$i/$1" ]]; then
        allSavs+=("$i/$1")
    fi
    #echo `find $i -name $1`
    #allSavs+=(`find $i -name $1`)
done

#find the latest save file
for i in ${allSavs[@]}
do
    if [[ $i -nt $latest ]]
    then
        latest=$i
    fi
done
echo the latest file is $latest, copying to rest of locations.

for i in ${dirArray[@]} 
do
    rsync -a $latest $i
done
