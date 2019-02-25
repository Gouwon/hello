# Google Youtube API를 이용하여 (검색어: "시니어코딩"),
# Snippet정보와 Statistics 정보를 100개 이상 MongoDB에 저장하고,
# 조회수가 높은 순으로 10개를 출력하는 코드를 작성하시오.
# (Collection 명: pythons)

def main():
    import json

    # lst = get("시니어코딩", 100)
    # write(lst)

    for items in get("시니어코딩", 100):
        save(collection, items)

    # file_location = "./youtube.js"
    # json_data = open(file_location).read()

    # jsonData = json.loads(json_data)
    # print(jsonData)



def get(q, il):
    from apiclient.discovery import build

    # API_KEY = ""  #본인의 API키
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    req = youtube.search().list(
        part='snippet',
        q=q,
        type='video'
    )

    i = il / 50
    j = 0
    while req:
        j += 1
        if ( j == i ): break
            
        res = req.execute()
        ids = []
        for item in res['items']:
            ids.append( item['id']['videoId'] )

        snippetRes = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(ids)
        ).execute()

        yield snippetRes['items']

        req = youtube.search().list_next(req, res)

def write(lst):
    import json
    
    file_location = "./youtube.js"
    with open(file_location, 'w', encoding="utf-8") as make_file:
        json.dump(lst, make_file, ensure_ascii=False, indent="\t")


def save(collection, items):
    for item in items:
        pprint(item)
        for k, v in item['statistics'].items():
            item['statistics'][k] = int(v)

    result = collection.insert_many(items)
    print('Affected docs is {}'.format(len(result.inserted_ids)))


def top10(collection):
    for item in collection.find().sort('statistics.viewCount', DESCENDING).limit(5):
        sts = item['statistics']
        snippet = item['snippet']
        print(">>", sts['viewCount'], snippet['title'])

if __name__ == "__main__":
    main()