# # students.csv 파일에 10명의 학생정보(이름,성별,나이,성적) 있습니다.
# # (홍길동,남,23,80)
# # 이 파일을 읽어 성적순으로 출력하되,
# # 이름은 홍** 형태로, 성적은 학점으로 표현, 총점과 평균을 구하시오.
# # 그리고 상위 50%의 학생은 별도로 이름과 성적만 출력하시오.

# # 1. 이 파일을 읽어 성적순으로 출력(sort or sorted)
# # 2. 이름은 홍** 형태로, 성적은 학점으로 표현(__str__)
# # 3. 총점과 평균을 구하라.(reduce)
# # 4. 평균 이상인 학생 이름, 성적 출력(filter)



# class Student:
#     def __init__(self, name, gender, age, score):
#         self.name = name
#         self.score = score
#         self.age = age
#         self.gender = gender

#     def __str__(self):
#         return

# ## 10명의 학생정보 입력.
# # with open("students.csv", "w", encoding="utf8") as file:
#     # file.write("이름,성별,나이,성적\n")
#     # file.write("김가람,남,23,80\n")
#     # file.write("박가비,여,24,90\n")
#     # file.write("강경종,남,24,70\n")
#     # file.write("서겨울,여,24,60\n")
#     # file.write("정대원,남,24,50\n")
#     # file.write("성나은,여,24,65\n")
#     # file.write("고대식,남,24,78\n")
#     # file.write("나기쁨,여,24,85\n")
#     # file.write("국기원,남,24,75\n")
#     # file.write("장나라,여,24,85\n")

# ## 파일을 읽어서 list에 저장.
# students = [ ]
# with open("students.csv", "r", encoding="utf8") as file:
#     for s in file:



#         students.append(s)

#     for i in len(students):
#         student_info = students[i].split(',')
    
#     print(student_info[0], student_info[1])

#     # students_file = [
#     #     Student()
#     # ]
    
#     # for i in len(students)
        

total_point = reduce(lambda x, y: x.score + y.score, students)
total_average = total_point / len(students)

rankings = filter()




