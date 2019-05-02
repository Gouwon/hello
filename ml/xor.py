from sklearn import svm, metrics
import pandas as pd

# 트레이닝 셋
xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

df = pd.DataFrame(xor_data)

print("head   >>> ", df.head)
print("shape  >>> ", df.shape)
print("columns>>> ", list(df.columns))
print("nrow   >>> ", len(df.index))

print('==========================')
print(df.loc[:, 0:1])
print('--------------------------')
print(df.loc[:, 2])
print('==========================')

clf = svm.SVC(gamma='auto')
clf.fit(df.loc[:, 0:1], df.loc[:, 2])   # 지도 데이터 , 데이터

testset = [(0, 1), (1, 0), (1, 1), (2, -1), (3, 1)]
pred = clf.predict(testset)

print("pred ==> ", pred)

score = metrics.accuracy_score([1, 1, 0, 1, 0], pred)

print("score ==> ", score)


while True:
    cmd = input("Input x y>> ")

    x, y = cmd.split(" ")

    t = [(int(x), int(y))]
    p = clf.predict(t)
    print("pred ==> ", p[0])
    p = clf.predict(t)[0]
    print("pred=", "참" if p == 1 else '거짓')