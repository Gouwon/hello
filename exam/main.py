def chname(list_element):
    first_name = list_element[0][0]
    return  str(first_name + "**")

def chgend(list_element):
    if list_element[1] == "남":
        return "M"
    else:
        return "F"

def chages(list_element):
    ages = ['90대', '80대', '70대', '60대', '50대', '40대', '30대', '20대', '10대']
    ages.reverse()
    return ages[int(list_element[2]) // 10 - 1]

def chgrad(list_element):
    g_grades = ['A', 'B', 'C', 'D', 'F']
    g_grades.reverse()
    score = int(list_element[3])
    if score == 100:
        return 'A'
    elif score < 50:
        return 'F'
    else:
        return g_grades[score // 10 - 5]

def chaddr(list_element):
    list_element[4].split(" ")
    addr_info = list_element[4].split(" ")
    return addr_info[1] + " " + addr_info[2]

def setdata(klist_element):
    name = chname(list_element)
    gender = chgend(list_element)
    ages = chages(list_element)
    grade = chgrad(list_element)
    addr = chaddr(list_element)
    return (name, gender, ages, grade, addr)

def sqlite3_input(data):
    import sqlite3

    conn = sqlite3.connect("./exam.db")
    with conn:
        cur = conn.cursor()
        sql = "insert into Student(name, gender, age, grade, addr) values(?,?,?,?,?)"
        cur.executemany(sql, data)
   
        conn.commit()


data = []
with open("./students.csv", "r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i == 0: 
            continue
        list_element = line.split(",")
        data.append(setdata(list_element))

sqlite3_input(data)




    
