#Find every file in locations given in dirs.txt, create it if it doesnt exist.
#find latest file (using -nt)
#cp latest file to other file locations

mapfile -t dirArray < dirs.txt

latest=`find "${dirArray[0]}" -name "$1"`
all=()
for i in "${dirArray[@]}"
do
    all+="$i/$1"
done