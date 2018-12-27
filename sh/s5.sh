#/bin/bash

if [ $# -eq 0 ]
    then echo "Input the filename, please.."
         echo "usage) ./s5.sh <file.txt>"
    else 
        DATE=`date +%Y-%m-%d`
        mv ${1} ${DATE}.txt
        ls
fi
