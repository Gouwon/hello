# def fn():
# 	print("fn called")

# def exp(x):
# 	return x ** 2

# def get_fruits():
# 	return ['오렌지', '사과', '바나나']
# print(get_fruits()[1])

# def get_name():
# 	return 'Kent', 'Beck'
# print(get_name())   # tuple형으로 반환됨.

# def full_name(first_name, last_name):
#     return first_name + " " + last_name
# name = get_name()
# print(name, full_name(1,2))

# def var_param(a, *vp):  #*가 있으면 vp가 몇개가 와도 상관없다.
#     print(type(vp))
#     print(a, len(vp), vp[len(vp) - 1]) #*자리에 적어도 1개값은 있어야 한다.
# var_param(1, 2, 3, 4)

# def default_param(a, vp = 100): #vp자리에 변수가 입력되지 않았으면, 기본값으로 100.
#     print(a, vp)
# default_param(1)

# 두 수를 받아서 사칙연산을 수행하는 함수를 만드시오.

# 두 수를 입력.
# user_input = input("계산할 값들을 넣으세요. : ")
# calculate = ["+", "-", "*", "/"]


# 사칙 연산의 종류.
def plus(a, b):
    result = a + b
    return result
def minus(a, b):
    result = a - b
    return result
def multiply(a, b):
    result = a * b
    return result
def divide(a, b):
    result = a / b
    return result
    
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

user_input = input("계산할 값들을 넣으세요. : ")
user_input_list = user_input.split(" ")

a = int(user_input_list[0])
b = int(user_input_list[2])
c = user_input_list[1]

if c == "+":
    result = plus(a, b)
elif c == "-":
    reult = minus(a, b)
    if a < b:
       result = plus(a, -b)
elif c == "*":
    result = multiply(a, b)
elif c == "/":
    if b == 0:
        result = "분모는 0이 될 수 없습니다."
    else:
        result = divide(a,b)
else:
    result = "정확하게 입력해주세요!"
print("계산값 : {}".format(result))

# def fn():
# 	print("fn called")

# def exp(x):
# 	return x ** 2

# def get_fruits():
# 	return ['오렌지', '사과', '바나나']
# print(get_fruits()[1])

# def get_name():
# 	return 'Kent', 'Beck'
# print(get_name())   # tuple형으로 반환됨.

# def full_name(first_name, last_name):
#     return first_name + " " + last_name
# name = get_name()
# print(name, full_name(1,2))

# def var_param(a, *vp):  #*가 있으면 vp가 몇개가 와도 상관없다.
#     print(type(vp))
#     print(a, len(vp), vp[len(vp) - 1]) #*자리에 적어도 1개값은 있어야 한다.
# var_param(1, 2, 3, 4)

# def default_param(a, vp = 100): #vp자리에 변수가 입력되지 않았으면, 기본값으로 100.
#     print(a, vp)
# default_param(1)

# 두 수를 받아서 사칙연산을 수행하는 함수를 만드시오.

# 두 수를 입력.
# user_input = input("계산할 값들을 넣으세요. : ")
# calculate = ["+", "-", "*", "/"]


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
# elif c == "*":
#     result = multiply(a, b)
# elif c == "/":
#     result = divide(a,b)
# else:
#     print("정확하게 입력해주세요!")
# print("계산값 : {:+5.0f}".format(result))