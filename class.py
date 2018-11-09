class   Square:
    def __init__(self):
        self.name = "넓이"
    
    def area(self, a, b):
        print("넓이", a, b)

class Rectangle(Square):
    def area(self, a, b):
        print("직사각형의 넓이 = ", a * b)
    

class Parallelogram(Square):
    def area(self, a, b):
        print("평행사변형의 넓이 = ", a * b)


r = Square()
직사각형 = Rectangle()
평행사변형 = Parallelogram()

r.area(40, 40)
직사각형.area(10,20)
평행사변형.area(20, 40)

