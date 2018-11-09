""" cmd = input("Input(usage : 이름, 나이, 성별) >> ")
print(cmd) 

cmds = cmd.split(',')
print(cmds[0], cmds[1], cmds[2])

for i in cmds: """



# # 입력 받은 값들을 list로 저장.
# # 입력 받은 값들을 찢으면서 index와 value로 저장.
# # for 문으로 print.
# cmd = input("Input(usage : 이름, 나이, 성별) >> ")  # cmd = a,b,c
# print(cmd)
# print(type(cmd))


# # 콤마 또는 3개의 값이 있는지!
# for i, value in enumerate(cmd):
#     # 값의 존재 여부 확인
#     if cmd == '':
#         print("정확히 입력하시오!")
#         exit()
#     elif(cmd[i] == ","):
#         cmds = cmd.split(",")                      # cmds = ['a', 'b', 'c']




# s = "abc"
# print(s[1])
# if ',' not in s:
#     print("no")

# if(s.find(',') == -1):
#     print("nooooo")




# im = "a,b,c"
# arr = [m for m in im.split(',')]
# print("arr = ", arr)

# outmsg = "당신의 이름은 {}. 나이는 {}, 성별은 {}입니다."
# for val in arr:
#     outmsg = outmsg.format(val, "{}", "{}")
# print(outmsg.format(arr[0], arr[1], arr[2]))




# 이름, 나이, 성별 입력
cmd = input("입 력 : 이름,나이,성별 >> ")

# 콤마값이 있는지 확인하기
if ',' in cmd:  #if cmd.find(",") == -1: 컴마가 없는지 물어봄.
    cmds = cmd.split(",")
    if len(cmds) == 3:
        outmsg = "당신의 이름은 {}. 나이는 {}, 성별은 {}입니다."
        print(outmsg.format(cmds[0], cmds[1], cmds[2]))
# 입력값이 3인지 확인하기    
    elif len(cmds) != 3:
        print("입력값이 충분하지 않습니다.")
        exit()
elif("," not in cmd):
    print("정확하게 입력하시요!")
    exit()


erro_msg = "정확히 입력하시오!"
isExistsComma = False
for i in cmd:
    if i == ",":
        isExistsComma = True
        break
if isExistsComma == False:
    print(erro_msg)
    exit()