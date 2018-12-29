import pymysql
import etl_mysql_util as mu

conn_dooodb_verify = mu.connect_mysql("dooodb")
conn_dodb_verify = mu.connect_mysql("dodb")

table_name = 'Subject'
column_name = "id, name, profm classroom"

with conn_dooodb_verify:
    dooo_cnt = mu.get_count(conn_dooodb_verify, table_name)
    dooo_smpls = mu.get_sample(conn_dooodb_verify, table_name, "5")

    cur = conn_dooodb_verify.cursor()
    sql = "select " + column_name + " from " + table_name + " order by rand() limit 5"
    cur.execute(sql)
    dooo_list = cur.fetchall()

with conn_dodb_verify:
    do_cnt = mu.get_count(conn_dodb_verify, table_name)
    do_smpls = mu.get_sample_verify(conn_dodb_verify, table_name, dooo_smpls)
        

    if dooo_cnt != do_cnt:
        print("Not Valid Count!! \n dooodb = ", dooo_cnt ,"\n dodb = ", do_cnt)
        exit()
    else:
        print("Count is OK")
        cur = conn_dodb_verify.cursor()
        
        # sql = "select " + column_name + " from " + table_name + " where id = %s"
        # for row in dooo_list:
        #     cur.execute(sql, row[0])
        #     r = cur.fetchone()
        #     if row[0] == r[0] and row[1] == r[1] and row[2] == r[2] and row[3] == r[3]:
        #         print(r, " OK")
        #     else:
        #         print(row, r, " Fail!!")

        sql = '''select id, name, prof, classroom from Subject where id = %s and name = %s and prof = %s and classroom = %s'''
        cur.executemany(sql, dooo_list)
        print(cur.fetchall(), cur.rowcount)


print("dooo_smpls = ", dooo_smpls)
print("do_smpls = ", do_smpls)

for i, j in enumerate(dooo_smpls):
    if dooo_smpls[i][0:4] == do_smpls[i][0:4]:
        print("OOOOOKKKKK")
    else:
        print("NOT MATCHED!!!!!")
    