import sqlite3


# open connection
conn = sqlite3.connect('test.db')

# open cursor
cursor = conn.cursor()

# create table
cursor.execute("""create table if not exists phonebook (name char(32), phone char(32), email char(64) primary key)""")

# insert record
cursor.execute("""insert into phonebook(name, phone, email) values(?, ?, ?)""", ('김범수', '021-445-2424', 'visual@bskim.com'))
id = cursor.lastrowid
print(id)

cursor.execute("""insert into phonebook(name, phone, email) values(?, ?, ?)""", ('박신혜', '021-322-1542', 'shinehye@park.com'))
id = cursor.lastrowid
print(id)

# select records
cursor.execute("""select name, phone, email from phonebook""")
rows = cursor.fetchall()
for row in rows:
    print('NAME: {}, PHONE: {}, EMAIL: {}'.format(*row))

# update record
cursor.execute("""update phonebook set phone=?, email=? where name=?""", ('070-1234-4567', 'bskim@gmail.com', '김범수'))

# select record
cursor.execute("""select name, phone, email from phonebook where name = ?""",('김범수',))
row = cursor.fetchone()
print(row)

# delete record
cursor.execute("""delete from phonebook where email=?""", ('bskim@gmail.com',))

# commit insert
conn.commit()

# select records
cursor.execute("""select name, phone, email from phonebook""")
rows = cursor.fetchall()
for row in rows:
    print('NAME: {}, PHONE: {}, EMAIL: {}'.format(*row))

# close cursor
cursor.close()

# close connection
conn.close()