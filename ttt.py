import os
import sys
import datetime
import time



now = datetime.datetime.now()
os.system('git add -all')


sa = sys.argv ## sys.argv[0] :  sys.argv[1]:msg

user_msg = input("Commit 메세지를 입력하세요. ")
print(user_msg)
exit()
sa[1] = user_msg

if sa[1] == "": #if len(sa) < 2:===> git.bash에서 실행할 때
    msg_default = now.strftime('%Y-%m-%d lecture')
    os.system('git commit -am {}'.format(msg_default))

else:
    os.system('git commit -am {}'.format(sa[1]))

os.system('git push')

time.sleep(5)
