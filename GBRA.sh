#Find every file in locations given in dirs.txt, create it if it doesnt exist.
#find latest file (using -nt)
#cp latest file to other file locations

if [ ! $1 ] 
then
    echo "usage: GBRA.sh [file]"
    exit 1
fi

mapfile -t dirArray < dirs.txt

allSavs=()

#find each save file that exists.
for i in ${dirArray[@]} 
do
    allSavs+=`find $i -name $1`
done

latest=${allSavs[0]}
echo $latest
#find the latest save file
for i in ${allSavs[@]}
do
    echo $i
    if [[ $i -nt $latest ]]
    then
        latest=$i
    fi
done
echo $latest