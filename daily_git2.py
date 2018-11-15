import os
import sys
import datetime
import time



now = datetime.datetime.now()
os.system('git add --all')


sa = sys.argv ## sys.argv[0] : 실행파일  sys.argv[1]:msg 

user_msg = input("Commit 메세지를 입력하세요. ")
print(len(sa))
print(user_msg)
print(type(user_msg))
print(len(user_msg))
has_msg = len(sa) >= 2


if has_msg: #if len(sa) < 2:===> git.bash에서 실행할 때
    msg_default = now.strftime('%Y-%m-%d lecture')
    os.system('git commit -am "{}"'.format(msg_default))

else:
    os.system('git commit -am "{}"'.format(user_msg))

os.system('git push')

time.sleep(5)