import sqlite3
import random

conn = sqlite3.connect("./db/test.db")

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")


name = list()


for i in range(100):
    sung = random.choice(fam_names)
    name_1 = random.choice(first_names)
    name_2 = random.choice(first_names)
    tuple_a = sung + name_1 + name_2
    tuple_b = (tuple_a ,)
    name.append(tuple_b)


# print(name)
data = tuple(name)
print(data)

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"
    cur.executemany(sql, data)

    conn.commit()