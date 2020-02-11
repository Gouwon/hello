import os
import json


FILE_NAME = 'ingredient-data.json'
FILE_LOCATION = os.path.join(os.path.dirname(__file__), FILE_NAME)

def get_json_data(FILE_LOCATION):
    with open(FILE_LOCATION) as f:
        data = json.load(f)
        result = []
        i = 0
        print(' ', type(data), len(data))
        for datum in data:
            i += 1
            result.append(datum)
            if len(result) == 100:
                yield result
                result = []
        yield result
        print(",,,,,,", i)
        

r = get_json_data(FILE_LOCATION)
sum = 0

for rr in r:
    sum += rrr
    # print('\n\n >>>>> ', rrr)
    # print(ii, len(rr))
    