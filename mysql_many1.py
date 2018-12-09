import random
import pymysql

num_list = ["0","1","2","3","4","5","6","7","8","9"] * 4

def mk_name():
    family_name_list = list("김이박최강고윤엄한배성백전황서천방지마피")
    first_names_list = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")
    family_name = "".join(random.choice(family_name_list))
    first_name = "".join(random.sample(first_names_list, 2))
    return  family_name + first_name

def mk_addr():
    municipality_list = ['서울시', '부산시', '경주시', '대구시', '인천시']
    borough_list = ['노원구', '성북구', '남동구', '북구', '서구', '강동구']
    dong_list = ['중계동', '야음동', '별내동', '상계동', '신사동', '갈매동', '제기동']
    municipality = "".join(random.choice(municipality_list))
    borough = "".join(random.choice(borough_list))
    dong = "".join(random.choice(dong_list))
    street_addr_1 = "".join(random.choices(num_list, k=3))
    street_addr_2 = "".join(random.choices(num_list, k=2))
    street_addr = street_addr_1 + "-" + street_addr_2 + "번지"

    household_num = random.choice(range(2))
    if household_num == 1:
        num_list2 = ["0","1","2","3","4","5","6","7","8","9"]
        ho_num = random.choice(range(1, 4))
        household = "".join(random.choices(num_list2, k=ho_num)) + "호"
        return municipality + " " + borough + " " + dong + " " + street_addr + " " + household
    else:
        return municipality + " " + borough + " " + dong + " " + street_addr

def mk_birth():
    year = random.choice(range(1960, 1999))
    month_list = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    month = random.choice(month_list)
    long_month = ["04", "06", "09", "11"]
    if month == "02":
        date_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
    elif month not in long_month:
        date_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28", "29", "30", "31"]    
    else:
        date_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28", "29", "30"]
    date = random.choice(date_list)
    return  str(year) + '-' + month + '-' + date

def mk_tel():
    tel_num = "".join(random.choices(num_list, k=4)) + "-" + "".join(random.choices(num_list, k=4))
    return '010-' + tel_num

def mk_email():
    id_num = random.choice(range(3, 7))
    id_char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t", "u", "v","w","x","y","z"]
    mail_id = "".join(random.choices(id_char, k=id_num)) + "".join(random.choices(num_list, k=id_num-1))
    return mail_id + "@gmail.com"

def mk_info():
    return (mk_name(), mk_addr(), mk_birth(), mk_tel(), mk_email())

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
        sql = "insert into Student(name, addr, birth, tel, email) values(%s,%s,%s,%s,%s)"
        cur.executemany(sql, data)

        conn.commit()


data = []

for i in range(1000):
    data.append(mk_info())

# print(data)

insert_db(data)
