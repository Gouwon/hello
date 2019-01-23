import melon_utils as mu
import re
import datetime
import codecs
import csv

now = datetime.datetime.now()
n = now.strftime('%Y%m%d')

url = "https://www.melon.com/chart/"
method = 'get'
html = mu.get_html(url, method)

selector = 'tbody tr'
html_tags = html.select(selector)
pattern = re.compile("'(.*)'")

saveFile = './results/melon_top_100_list({}).csv'.format(n)
print(saveFile)
with codecs.open(saveFile, 'w', 'utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"')
    for html_tag in html_tags:
        rank = html_tag.select_one("span.rank").text
        songId = html_tag.get('data-song-no')
        title = html_tag.select_one('div.ellipsis.rank01').text.strip()
        artist = ",".join([artist_name.text for artist_name in html_tag.select('div.ellipsis.rank02 span a')])
        albumId = re.findall(pattern, html_tag.select_one('div.wrap a').get('href'))[0]
        albumTitle = html_tag.select_one('div.wrap a').get('title')

        result = [rank, songId, title, artist, albumId, albumTitle]
        print(rank, songId, title, artist, albumId, albumTitle)
        print("===================")
        writer.writerow(result)
print("+++++++++++++++++++++++++++", saveFile, " saved +++++++++++++++++++++++++++")