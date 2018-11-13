class Student:
    def __init__(self):
        self.name = Name
        self.score = score

    def __str__(self):
        return "{}:{}".format(self.name, self.score)


students = [
    Student("김일수", 10)
    Student("김삼수", 30)
    Student("김이수", 20)
]

print(student[0])

def print_students():
    print("------------------")
    for s in students:
        print(s)

studunts = sorted(student, key = lambda stu: stu.score)
print_students()

studunts = sort(key = lambda stu: stu.score)
print_students()