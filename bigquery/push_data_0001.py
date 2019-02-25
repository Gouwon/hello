import bigquery
import sys

client = bigquery.get_client(json_key_file='bigquery.json', readonly=False)

DATABASE = "bqdb"
TABLE = "Test"
if not client.check_table(DATABASE, TABLE):
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

    client.create_table(DATABASE, TABLE, [
        {'name': 'songno', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'albumid', 'type': 'string', 'description': 'album id'},
    ])

ttt = [ {'songno': '111', 'title': '홍1', 'albumid': '121212121', 'rec':{'sub1':'abc1'}},
        {'songno': '222', 'title': '홍2', 'albumid': '121212121', 'rec':{'sub1':'def2'}},
        {'songno': '333', 'title': '홍3', 'albumid': '121212121', 'rec':{'sub1':'ghi3'}} ]
pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
print("Pushed Result is", pushResult)