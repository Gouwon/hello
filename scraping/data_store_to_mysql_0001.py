import pymysql
import codecs
import csv

def connect_mysql(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='root1!',
        port=3306,
        db=db,
        charset='utf8')

## mysql db table 생성
conn_doodb = connect_mysql("dooodb")

with conn_doodb:
    cur = conn_doodb.cursor()
    cur.execute("drop table if exists MelTop100")
    sql_create = '''
                create table MelTop100(
                    id smallint not null auto_increment,
                    title varchar(128),
                    artist varchar(128),
                    ranking smallint,
                    likecnt int default 0 not null,
                    likeDiff int default 0 not null,
                    primary key(id)
                )
                '''
    cur.execute(sql_create)
print("----- Table Create Complete -----")

## codecs 모듈로 csv파일 읽어 들이기
csvFile = "./results/data/melon_top_100_list.csv"
csvFile_encoded = codecs.open(csvFile, "r", "utf-8")
reader = csv.reader(csvFile_encoded, delimiter=',', quotechar='"')

p = list(reader)
pp = len(p)

## dooodb에 데이터 입력하기
insert_sql = "insert into MelTop100(ranking, title, artist, likecnt, likeDiff) values(%s,%s,%s,%s,%s)"
with conn_doodb:
    cur = conn_doodb.cursor()
    for i, cells in enumerate(p):
        if i == 0 or i == pp - 1: 
            continue
        else: 
            print(cells)
            cur.execute(insert_sql, cells)
    print("AffectedRowCount is ", cu.rowcount)


