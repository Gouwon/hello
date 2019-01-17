import random
from pprint import pprint
data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

results = {}
for keys in data:
    # pprint(data[keys])
    ys = len(data[keys])
    xs = len(data[keys][0])
    sum1 = 0
    sum2 = 0
    for x in range(xs):
        sum1 += data[keys][x][x]
        sum2 += data[keys][x][4-x]
    result = sum1 + sum2
    results[keys] = result

# s_ms = sorted(ms.items(). key=lambda x: x[1])
# s_ms[0][0]
# s_ms = min(ms, key=lambda k: ms[k])
results_value = min(y for x, y in results.items())
print(results_value)
for r in results:
    if results_value == results[r]: 
        print(r)
    else: continue