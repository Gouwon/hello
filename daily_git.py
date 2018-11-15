#coding=utf-8

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