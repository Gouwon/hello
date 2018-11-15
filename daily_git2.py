import os
import sys
import datetime
import time

now = datetime.datetime.now()
os.system('git add --all')

sa = sys.argv ## sys.argv[0] : 실행파일  sys.argv[1]:msg 

user_msg = input("Commit 메세지를 입력하세요. ")
has_msg = len(sa) >= 2 ## 2보다 크거나 같으면 true, 작으면 false

if has_msg: #if len(sa) < 2:===> git.bash에서 실행할 때
    msg_default = now.strftime('%Y-%m-%d lecture') ## 2018-11-15 lecture
    os.system('git commit -am "{}"'.format(msg_default))

else:
    os.system('git commit -am "{}"'.format(user_msg))

os.system('git push')

print("커밋이 완료되었습니다. \n 수고하셨습니다.")
time.sleep(5)
exit()