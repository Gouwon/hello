#/bin/bash

PRE_IFS=$IFS

IFS="
"

cd /home/dooo
Filename="bin_files.txt"
touch $Filename

sum=0

for i in `ls -al /bin`
    do
        name=`echo ${i} | awk '{print $9}'`
        fileuse=`echo ${i} | awk '{print $5}'`

        #arr=(`echo ${i} | awk '{print $9}'` `echo ${i} | awk '{print $5}'`)
        #echo "${arr[0]} ${arr[1]} ${arr[@]}"


        #if [ "$F" == "." ] || [ "$F" == ".." ] || [ "$F" == "" ]
        if [ "${name}" == "." ]; then
             continue
        elif [ "${name}" == ".." ]; then 
            continue
        elif [ "${name}" == "" ];then 
            continue
        else
            echo " ${name} =================> ${fileuse}" >> $Filename
            sum=`expr $fileuse + $sum`
        fi
    done

echo "Total size of /bin directory is ${sum}." >> $Filename

IFS=$PRE_IFS
