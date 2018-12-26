#/bin/bash

cat ~/*.txt

for i in `ls *.txt`
    do cat ${i}
    done

for i in `ls *.txt`
    do 
     echo "-----------------------------------------------------"
     echo ${i}
     cat ${i}
     echo "====================================================="
    done
    
