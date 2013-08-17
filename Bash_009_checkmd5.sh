#! /bin/bash

while read line
do
    echo $line
    a=$(echo -n "$line" | md5sum | awk '{ print $1 }')
    #echo $a
    if [ $a = "4d6bfce7c3d01def4625e405087939ed" ]; then
        echo "Ya esta"
        echo $line
        echo $line > OK.txt
    fi
done < diccionario.txt
