import pymysql
import cx_Oracle

def connect_mysql(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='root1!',
        port=3306,
        db=db,
        charset='utf8')

def connect_oracle():
    return cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")

    
def get_count(conn, tbl, where = ''):
    cur = conn.cursor()
    sql = "select count(*) from " + tbl
    if where != '':
        sql = sql + " where " + where

    # print("get_count.sql=", sql)
    cur.execute(sql)
    return cur.fetchone()[0]

def trunc_table(conn, tbl):
    cur = conn.cursor()
    cur.execute('truncate table ' + tbl)
    return cur.rowcount

def get_sample(conn, tbl, n):
    cur = conn.cursor()
    sql = "select * from " + tbl + " order by rand() limit " + n
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

def get_sample_verify(conn, tbl, smpls):
    cur = conn.cursor()
    rows = []
    for smpl in smpls:
        sql = "select * from " + tbl + " where id = %s"
        cur.execute(sql, smpl[0])
        rows.append(cur.fetchone()) 
    return rows
        
