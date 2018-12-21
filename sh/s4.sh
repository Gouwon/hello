#/bin/bash


if [ $# -gt 0 ]
   then cat ${1}
   else printf "파일명을 입력하세요!\n"
        echo "파이일명을 
        입력하세요!"
fi

if [ $# -eq 0 ]
    then
    echo "Input the filename, please.."
    echo "usage) ./s4.sh <format-file> <date-file> <test-file>" 
    exit 0
fi

cat ${1}
