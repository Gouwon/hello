from sklearn import svm, metrics
import pandas as pd

dataset = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
    [3, 1, 0],
    [3, 3, 1],
    [4, 4, 1],
    [-5, -5, 1],
    [6, 5, 1]

]

df = pd.DataFrame(dataset)

clf = svm.SVC(gamma='auto')
print(df.loc[:, 2])
clf.fit(df.loc[:, 0:1], df.loc[:, 2])

testset = [(0, 1), (1, 0), (1, 1), (-2, -2), (3, 1), (0, 0)]
pred = clf.predict(testset)

print("pred ==> ", pred)

score = metrics.accuracy_score([0, 0, 1, 1, 0, 1], pred)

print("score ==> ", score)

while True:
    cmd = input("Input x y>> ")

    x, y = cmd.split(" ")

    t = [(int(x), int(y))]
    p = clf.predict(t)
    print("pred ==> ", p[0])
    p = clf.predict(t)[0]
    print("pred=", "참" if p == 1 else '거짓')