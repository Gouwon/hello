import pymysql


def connect_sql(dbname):
    return pymysql.connect(
    host='localhost', 
    user='dooo', 
    password='root1!', 
    port=3306, 
    db=dbname, 
    charset='utf8')

## dooodb 연결
conn_dooodb = connect_sql("dooodb")


## dooodb 읽어들이기 및 읽어들인 것 저장
data = []
with conn_dooodb:
    cur_dooodb = conn_dooodb.cursor() 
    sql_dooodb = "select * from Subject"
    cur_dooodb.execute(sql_dooodb)
    rows_dooodb = cur_dooodb.fetchall()

    conn_dooodb.commit()

for row in rows_dooodb:
    # print(row[0:4])
    print(rows_dooodb)

## dodb 연결
conn_dodb = connect_sql("dodb")

## dodb에 데이터 입력하기.
with conn_dodb:
    cur_dodb = conn_dodb.cursor() 
    cur_dodb.execute('truncate table Subject')
    sql_dodb = "insert into Subject(id,name,prof,classroom) values(%s,%s,%s,%s)"
    # cur_dodb.executemany(sql_dodb, rows_dooodb)
    for row in rows_dooodb:
        cur_dodb.execute(sql_dodb, row[0:4])
    print("AffectedRowCount is ", cur_dodb.rowcount)


    conn_dodb.commit()

