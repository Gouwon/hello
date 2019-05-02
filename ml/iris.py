from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

csv = pd.read_csv('./data/iris.csv')       # csv[:4] : 0 ~ 4행
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)

clf = svm.SVC(gamma='auto')  # 학습
clf.fit(trainData, trainLabel)

pred = clf.predict(testData)    # 검증
score = metrics.accuracy_score(testLabel, pred)
print(score)

t = [(5.1,3.5,1.4,0.2)] # 확인
r = clf.predict(t)
print(">>>>", r)