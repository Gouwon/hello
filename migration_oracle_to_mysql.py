import etl_mysql_util as mu

conn_oracle = mu.connect_oracle()
conn_mysql = mu.connect_mysql("dodb")


with conn_oracle:
    # cursor를 만들어줍니다
    cursor = conn_oracle.cursor()

    sql = '''select region_id, region_name from Regions'''
    
    cursor.execute(sql)
    rows = cursor.fetchall()

for row in rows:
    print(row)

conn_mysql = mu.connect_mysql("dodb")

with conn_mysql:
    cur_mysql = conn_mysql.cursor()
    cur_mysql.execute("drop table if exists Region")
    sql_create = '''
                create table Region(
                    id smallint not null,
                    name varchar(36),
                    primary key(id)
                )
                '''
    cur_mysql.execute(sql_create)

    sql_insert = "insert into Region(id, name) values(%s, %s)"
    cur_mysql.executemany(sql_insert, rows)

    print("AffectedRowCount is ", cur_mysql.rowcount)