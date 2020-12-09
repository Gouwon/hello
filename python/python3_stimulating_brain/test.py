# import os
# import sys
# import time

# class TEST():
#     def test(
#             self, var_one, var_two,
#             var_three, var_four
#     ):
#         """
#         this is test function.
#         should use for test only.
#         this section is for block comments.
#         """
#         print('{} {}\n{} {}'.format(var_one, var_two, var_three, var_four))

# print('hello, world!!')
# print('{} {} {}'.format(os.path.basename(__file__), sys.argv[0], time.localtime()))
# test1 = TEST()
# test1.test(1,2,3,4)

# for i in range(1,6):
#     print("*" * i)

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(1,6):
#     print("*" * (6-i))

# for i in range(1, 6):
#     for j in range(6 - i):
#         print("*", end="")
#     print()

# loop_no = 1
# while(loop_no < 6):
#     print("*" * loop_no)
#     loop_no += 1


# loop_no = 1
# while(loop_no < 6):
#     print("*" * (6 - loop_no))
#     loop_no += 1


# while True:
#     user_input_str = input("반복횟수를 입력하세요 : ")
    
#     try:
#         user_input_int = int(user_input_str)
#         if user_input_int <= 0:
#             print("0보다 작거나 같은 수는 입력할 수 없습니다.")
#             break
#         else:
#             for i in range(1, user_input_int + 1):
#                 print("*" * i)
#     except Exception as err:
#         print(err)

# def average(*args):
#     if args and 0 not in args:
#         return sum(args) / len(args)

# average(1,2,3,4,5)

# def draw_inverted_triangle(start):
#     if start > 0:
#         start += 1
#         for i in range(1, start):
#             print("*" * (start - i))

# draw_inverted_triangle(10)

# import struct

# packed = struct.pack('i', 123)
# for b in packed:
#     print(b)

# def plus_or_minus(arg):
# 	if arg < 0:
# 		return "minus"
# 	elif arg > 0:
# 		return "plus"

# result = plus_or_minus(0)
# print(result)

import calculator.plus
print(str(plus(1, 2)))

# d = {'spam': 1, 'eggs': 2, 'cheese':3}
# e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

# print(d|e)
# print(e|d)