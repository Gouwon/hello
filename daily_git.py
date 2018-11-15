#coding=utf-8
# import os
# import sys
# import datetime

# def mysis():
#     if os.name == 'nt':
#         os.system('CLS')
#     else:  # posix
#         os.system('clear')

# now = datetime.datetime.now()
#  ## sys.argv[0] :  sys.argv[1]:msg
# os.system('git add -all')


# sa = sys.argv
# sa[1] = user_msg

# if sa[1] != "n": #if len(sa) < 2:===> git.bash에서 실행할 때
#     msg_default = now.strftime('%Y-%m-%d lecture')
#     os.system('git commit -am {}'.format(msg_default))

# else:
#     sa[1] = input("Write Massage : ")
#     sa[1] = str(sa[1])
#     os.system('git commit -am {}'.format(sa[1]))

# os.system('git push')

import sys
import os
import datetime

def gitcmd(cmd):
    print("gitcmd>>> ", cmd)
    os.system(cmd)

sa = sys.argv   # [0]:실행파일, [1]:메시지 부분
now = datetime.datetime.now()
default_msg = "{} lecture".format(now.strftime('%Y-%m-%d'))
commit_msg = default_msg
has_msg = len(sa) >= 2
# if  len(sa) == 1:   # 메세지가 입력이 안되었을 때.

if has_msg:
    commit_msg = sa[1]

else:
    input_msg = input("Default Message??  (Yes: Enter or input message) >> ")
    if input_msg != '': # msg가 있을 경우,
        commit_msg = input_msg 

print("committing......", commit_msg)

gitcmd("git add --all")
gitcmd('git commit -am "{}"'.format(commit_msg))
gitcmd("git push")