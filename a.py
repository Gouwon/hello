class TestClass:
    name = "TEST"

    def __init__(self):
        print("kkkkkkkkkkkkk")

    def static_method():
        print("STATIC!!")

    def get_name(self):
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("My init!!!")

    def get_name(self):
        t = super().get_name()
        return "Chiled Name : " + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2

test = TestClass()
child = Child()

cmd = input("Input the function name>> ")

getattr(test, cmd)() ## 클래스를 만들었을 때, 코드를 
getattr(TestClass,'static_method')()

# print(" >>>>>>> ", test.get_name(), child.get_name())

# c = callable(test.get_name)
# print(" >>>>>> ", c)