import melon_utils as mu 
import codecs
import csv

mu.get_top100list()

csvFile = codecs.open('./results/melon_top_100_list(20190123).csv', 'r', 'utf-8')
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

sql = 'insert into MelList(SongId, AlbumId) values(%s, %s)'
lst = []
for row in reader:
    lst = (row[1], row[4])
    mu.insert_data_to_db("dooodb", sql, lst)

print("=============== MelList Insert Completed! =================")

url = "https://www.melon.com/album/detail.htm"
params = {"albumId" : albumno }
html = mu.get_html(url, 'get', params=params)
