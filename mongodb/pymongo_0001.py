import requests, json
from bs4 import BeautifulSoup
from pymongo import MongoClient, DESCENDING

## Naver API를 이용하여 "파이썬"으로 검색된 책들의 정보를 dooodb.Books Collection에 담아보시오.
## Books collection에서 가격순으로 10개를 출력하시오.

def put():
    url = "https://openapi.naver.com/v1/search/book.json"

    title = "파이썬"
    params = {
        "query": title,
        "display": 100,
        "start": 1,
        "sort": "date"
    }

    headers = {
        "X-Naver-Client-Id": "nfSbPUyZrzsu6ycI7DRr",
        "X-Naver-Client-Secret": "oMFYO0EzLu"
    }

    result = requests.get(url, params=params, headers=headers).text

    jsonData = json.loads(result)


    mongo_client = MongoClient('localhost', 27017)

    collection = mongo_client.testdb.Books

    result = collection.insert_many(jsonData["items"])

    print('Affected docs is {}'.format(len(result.inserted_ids)))



def get():
    mongo_client = MongoClient('localhost', 27017)
    testdb = mongo_client.get_database('testdb')
    collections = testdb.list_collection_names()
    Books = testdb.get_collection('Books')

    results = Books.find({}, {"price":1}).sort('price', DESCENDING).limit(10)
    for result in results:
        print(result)


### mongoDB에서 
# var cur = db.test.Books.find()
# cur.forEach


if __name__ == "__main__":
    get()
