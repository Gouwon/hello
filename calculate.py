# 사칙 연산의 종류.
# def plus(a, b):
#     result = a + b
#     return result
# def minus(a, b):
#     result = a - b
#     return result
# def multiply(a, b):
#     result = a * b
#     return result
# def divide(a, b):
#     result = a / b
#     return result
    
# 입력값이 정확하지 않으면 다시 입력.

# for i in calculate:
#     if i in user_input:
#         user_input_list = user_input.split(" ")
#         a = int(user_input_list[0])
#         b = int(user_input_list[2])
#         c = user_input_list[1]
#         if c == "+":
#             result = plus(a, b)
#             break
#         elif c == "-":
#             result = minus(a, b)
#             break
#         elif c == "*":
#             result = multiply(a, b)
#             break
#         elif c == "/":
#             result = divide(a, b)
#             break
#         else:
#             print("계산값을 확인해 주세요.")
#             break

# print("계산값 : {:5.0f}".format(result))

# user_input = input("계산할 값들을 넣으세요. : ")
# user_input_list = user_input.split(" ")

# a = int(user_input_list[0])
# b = int(user_input_list[2])
# c = user_input_list[1]

# if c == "+":
#     result = plus(a, b)
# elif c == "-":
#     reult = minus(a, b)
#     if a < b:
#        result = plus(a, -b)
# elif c == "*":
#     result = multiply(a, b)
# elif c == "/":
#     if b == 0:
#         result = "분모는 0이 될 수 없습니다."
#     else:
#         result = divide(a,b)
# else:
#     result = "정확하게 입력해주세요!"
# print("계산값 : {}".format(result))

##========================================================

# def plus(a, b):
#     return a + b

# def minus(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     if b == 0:
#         return a

#     return a / b


# while(True):
#     cmd = input("수식을 입력하세요(usage: 2 + 3)> ")
#     print("cmd = ", cmd)
#     cmds = cmd.split(' ')
#     print("cmds = ", cmds)

#     if cmd == 'q':
#         print("계산기를 종료합니다.")
#         break

#     else:
#         # @Try cmds 하나만으로 set해보기
#         # a, op, b = int(cmds[0]), cmds[1], int(cmds[2])
#         a, op, b = cmds
#         # print("a= ", a, "op= ", op, "b= ", b)
#         a, op, b = int(cmds[0]), cmds[1], int(cmds[2])
#         a, b = int(a), int(b)


#         if op == '+':       #가장 많이 쓸 만한 것으로 먼저 쓴다.
#             r = plus(a, b)  #테스트할 때는 쉬운 것부터.

#         elif op == '-':
#             r = minus(a, b)

#         elif op == '*':
#             r = mul(a, b)

#         else:
#             r = div(a, b)

#         if op in '+-*':
#             print("Answer is {:d}".format(r))
#         else:
#             print("Answer is {:f}".format(r))


# ##===========================

# def plus(a, b):
#     return a + b

# def minus(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     if b == 0:
#         return a

#     return a / b


# def input_calc():
#     cmd = input("수식을 입력하세요(usage: 2 + 3)> ")
#     print("cmd = ", cmd)
#     cmds = cmd.split(' ')
#     print("cmds = ", cmds)

#     if cmd == 'q':
#         print("계산기를 종료합니다.")
#         break

#     else:
#         # @Try cmds 하나만으로 set해보기
#         # a, op, b = int(cmds[0]), cmds[1], int(cmds[2])
#         a, op, b = cmds
#         # print("a= ", a, "op= ", op, "b= ", b)
#         a, op, b = int(cmds[0]), cmds[1], int(cmds[2])
#         a, b = int(a), int(b)


#         if op == '+':       #가장 많이 쓸 만한 것으로 먼저 쓴다.
#             r = plus(a, b)  #테스트할 때는 쉬운 것부터.

#         elif op == '-':
#             r = minus(a, b)

#         elif op == '*':
#             r = mul(a, b)

#         else:
#             r = div(a, b)

#         if op in '+-*':
#             print("Answer is {:d}".format(r))
#         else:
#             print("Answer is {:f}".format(r))

# while(True):
#     cmds = user_input()
#     input_calc(cmds)