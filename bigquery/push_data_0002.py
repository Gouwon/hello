import pymysql
from collections import namedtuple

import bigquery
import sys

from pprint import pprint

def connect_mysql(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='root1!',
        port=3306,
        db=db,
        charset='utf8')

# class Song:
    
def fn1():
    conn_doodb = connect_mysql("dooodb")

    with conn_doodb:
        cur = conn_doodb.cursor()
        sql_select = '''select cast(id as char) as id, songId, title, genre, albumId from Song limit 100'''
        cur.execute(sql_select)

        # cols = [c[0] for c in cur.description]
        # Song = namedtuple('Song', " ".join(cols))
        # dset = [Song(*r)._asdict() for r in rows]

        rows = cur.fetchall()

        song_keys = " ".join(i[0] for i in cur.description)
        Song = namedtuple('Song', song_keys)
        dset = [Song(*r)._asdict() for r in rows]

    return dset

def fn2():
    conn_doodb = connect_mysql("dooodb")

    with conn_doodb:
        cur = conn_doodb.cursor()
        sql_select = '''select cast(id as char) as id, albumId, title, cast(releaseDate as char) as releaseDate, cast(score as char) as score, publisher, label         from Album limit 100'''
        cur.execute(sql_select)

        # cols = [c[0] for c in cur.description]
        # Song = namedtuple('Song', " ".join(cols))
        # dset = [Song(*r)._asdict() for r in rows]

        rows = cur.fetchall()

        album_keys = " ".join(i[0] for i in cur.description)
        Album = namedtuple('Album', album_keys)
        dset_album = [Album(*r)._asdict() for r in rows]    
    
    return dset_album

def fn3(Data):
    client = bigquery.get_client(json_key_file='bigquery.json', readonly=False)

    DATABASE = "bqdb"
    TABLE = "Songs"
    data = Data
    # pprint(data)
    if not client.check_table(DATABASE, TABLE):
        print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

        client.create_table(DATABASE, TABLE, [
            {'name': 'id', 'type': 'integer', 'description': 'mysql id'},
            {'name': 'songId', 'type': 'string', 'description': 'song id'},
            {'name': 'title', 'type': 'string', 'description': 'song title'},
            {'name': 'genre', 'type': 'string', 'description': 'genre'},
            {'name': 'albumId', 'type': 'string', 'description': 'album id'},
            {'name': 'album', 'type': 'record', 'description': 'album info',
             'fields':[
                 {'name': 'id', 'type': 'integer', 'descripition': 'mysql album id'},
                 {'name': 'albumId', 'type': 'string', 'descripition': 'album id'},
                 {'name': 'title', 'type': 'string', 'descripition': 'album string'},
                 {'name': 'releaseDate', 'type': 'TIMESTAMP', 'descripition': 'album releaseDate'},
                 {'name': 'score', 'type': 'numeric', 'descripition': 'album score'},
                 {'name': 'publisher', 'type': 'string', 'descripition': 'album publisher'},
                 {'name': 'label', 'type': 'string', 'descripition': 'album label'}]}
        ])
 
    pushResult = client.push_rows(DATABASE, TABLE, data, insert_id_key='songId')
    print("Pushed Result is", pushResult)


if __name__ == "__main__":
    dset = fn1()
    dset_album = fn2()

    i = 0
    data = []
    for d in dset:
        d['fields'] = dset_album[0]
        data.append(d)
    
    # print(type(data))
    # for dd in data:
    #     print(type(dd))
    #     pprint(dd)
    #     pprint(dd['fields'])
    #     break
    # pprint(data)
    # fn3(data)
            
    # getData()
    # pushData()