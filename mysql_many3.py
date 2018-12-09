import random
import pymysql

num_list = ["0","1","2","3","4","5","6","7","8","9"] * 4

def mk_name():
    family_name_list = list("김이박최강고윤엄한배성백전황서천방지마피")
    first_names_list = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")
    family_name = "".join(random.choice(family_name_list))
    first_name = "".join(random.sample(first_names_list, 2))
    return  family_name + first_name


def mk_info():
    return (mk_name(),)

def insert_db(data):
    conn = pymysql.connect(
        host='localhost', 
        user='gouwon', 
        password='root1!', 
        port=3306, 
        db='study', 
        charset='utf8')


    with conn:
        cur = conn.cursor() 
        sql = "insert into Prof(name) value(%s)"
        cur.executemany(sql, data)

        conn.commit()


data = []

for i in range(10):
    data.append(mk_info())

# print(data)

insert_db(data)
