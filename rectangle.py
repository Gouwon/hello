# 사각형의 종류를 선택하고, 가로와 세로를 입력받아서, 그 넓이를 구하는 프로그램

# 사각형의 종류를 선택.
# print("사각형의 종류는?\n 1) 정사각형\n 2) 직사각형\n 3) 평행사변형")

# # 부모 class - 사각형 만들기
# class Quadrangle():
#     def __init__(self):
#         self.name = "quadrangle"
    
#     def user_input(self, a, b): #self가 없으면 static method --> 명세쪽에 만듦.
#         user_input_measure = input("계산할 사각형의 수치를 입력하세요.(ex : 1, 2)")
#         user_input_measure_list = user_input_measure.split(",")
#         a, b = user_input_measure_list[0], user_input_measure_list[2]

#     def area(self, a, b):
#         print("사각형의 넓이 = ", a * b)
    
# class Square(Quadrangle):
#     def user_input(self, a):
#         user_input_measure = input("계산할 정사각형의 수치를 입력하세요.(ex : 2)")
#         a = int(user_input_measure[0])
#         return a
    
#     def area(self, a):
#         print("정사각형의 넓이 = ", a ** 2)
#         return a ** 2

# class Rectangle(Quadrangle):
#     def user_input(self, a, b):
#         user_input_measure = input("계산할 직사각형의 수치를 입력하세요.(ex : 1, 2)")
#         user_input_measure_list = user_input_measure.split(",")
#         a, b = int(user_input_measure_list[0]), int(user_input_measure_list[1])
#         return a, b
    
#     def area(self, a, b):
#         print("직사각형의 넓이 = ", a * b)
#         return a * b

# class Parallelogram(Quadrangle):
#     def user_input(self, a, b):
#         user_input_measure = input("계산할 직사각형의 수치(밑변과 높이)를 입력하세요.(ex : 2, 3)")
#         user_input_measure_list = user_input_measure.split(",")
#         a, b = int(user_input_measure_list[0]), int(user_input_measure_list[1])
#         return a, b ## 튜플로 반환됨.

    
#     def area(self, a, b):
#         print("평행사변형의 넓이 = ", a * b)
#         return a * b


# # 사각형의 종류를 입력받는 부분
# user_input = input("계산할 사각형을 선택하세요.(ex : 1) : ")
# print("user_input = ", user_input)

# # 사각형의 가로, 세로를 입력받는 부분
# # user_input_measure = input("계산할 사각형의 수치를 입력하세요.(ex : 1, 2)")
# # user_input_measure_list = user_input_measure.split(",")

# #넓이를 구하는 부분.
# a, b = 5, 5

# if user_input == "1":
#     square = Square()
#     a = square.user_input(a)
#     print(square.area(a))

# elif user_input == "2":
#     rectangle = Rectangle()
#     tmp = rectangle.user_input(a, b)
#     a, b = tmp
#     print(rectangle.area(a, b))

# elif user_input == "3":
#     parallelogram = Parallelogram()
#     tmp = parallelogram.user_input(a, b)
#     a, b = tmp
#     print(parallelogram.area(a, b))


##==============================================================================
## 참고답안1

# def to_int(s):  #전역함수
#     if type(s) == str:
#         return int(s)
#     else:
#         return s

# class 사각형:
#     x, y = 0, 0
    
#     def __init__(self):
#         print("사각형 created")
    
# class 직사각형(사각형):
#     def 넓이(self, x, y):
#         return to_int(x) * to_int(y)

# class 평행사변형(사각형):
#     def 넓이(self, x, y):
#         return to_int(x) * to_int(y)

# while True:

#     rect_type = input("사각형의 종류는?\n 1) 직사각형\n 2) 평행사변형\n (quti:q)>> ")

#     if rect_type == "q":
#         break

#     if rect_type == "1":
#         rect1 = 직사각형()
#         가로_세로 = input("가로와 세로는??(usage : 가로,세로) ")
#         가로, 세로 = 가로_세로.split(',')
#         결과 = rect1.넓이(가로, 세로)
#         #직사각형.넓이(가로, 세로)
#         print("직사각형의 넓이는 {}입니다. \n".format(결과))

#     else:
#         rect2 = 평행사변형()
#         밑변_높이 = input("밑변과 높이는??(usage : 밑변,높이) ")
#         밑변, 높이 = 밑변_높이.split(',')
#         결과 = rect1.넓이(밑변, 높이)
#         #직사각형.넓이(가로, 세로)
#         print("평행사변형의 넓이는 {}입니다. \n".format(결과))

##=================================================
# 참고답안 2

class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class 사각형:
    name = "사각형"
    msg = "가로와 세로는??"
    def __init__(self):
        print("사각형 created")

    def input_data(self):
        datum = input(self.msg)  # 5, 3
        data = datum.split(',')  # ['5', '3']
        x, y = Casting.to_int(data[0]), Casting.to_int(data[1])
        self.__새넓이(x, y)

    def __새넓이(self, x, y):
        r = x * y
        print("{}의 넓이는 {}입니다".format(self.name, r))

class 직사각형(사각형):
    name = "직사각형"
    msg = "가로와 세로는?? (usage: 가로,세로)"
    
class 평행사변형(사각형):
    name = "평행사변형"
    msg = "밑변와 높이는?? (usage: 밑변, 높이)"









all_rects = [직사각형(), 평행사변형()]

while True:
    print()
    rect_type = input("사각형의 종류는?\n 1) 직사각형\n 2)평행사변형\n (quit:q) >> ")
    if (rect_type == 'q'):
        break

    rect_index = Casting.to_int(rect_type) - 1
    rect = all_rects[rect_index]
    rect.input_data()