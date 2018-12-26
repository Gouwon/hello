#/bin/bash

if [ $# -eq 0 ]
    then
        echo "InputError : Filename not found."
        echo "usage) bash ./s51.sh <file1.txt> <file2.txt>"
    else
        DATE=`date +%Y-%m-%d --date='1 day ago'`
        cat ${1} ${2} > ${DATE}.log
        ls        
fi
