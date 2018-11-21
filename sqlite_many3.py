import sqlite3
import random


fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

def make_name():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))
    # print(type(sung), type(name))
    return (sung + name, )

# print(make_name())

data = list()
print(data)

for i in range(100):
    data.append(make_name())

conn = sqlite3.connect("./db/test.db")

with conn:
    cur = conn.cursor() ## sqlsequence 의 다음 값에 insert가 되도록 커서가 위치를 잡아줘야 한다.    ``
    sql = "insert into Student(name) values(?)"
    cur.executemany(sql, data)

    conn.commit()