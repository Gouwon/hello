from apiclient.discovery import build
from pprint import pprint

# API_KEY = ""  #본인의 API키

youtube = build('youtube', 'v3', developerKey=API_KEY)
req = youtube.search().list(
    part='snippet',
    q='파이썬',
    type='video'
)

i = 0
while req:
    i += 1
    if ( i > 2): break
        
    search_res = req.execute()
    for item in search_res['items']:
        pprint(item)

    req = youtube.search().list_next(req, search_res)

    print(len(search_res['items']), "\n")
