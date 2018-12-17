## fruits = {'오렌지': 400, '사과': 200, '바나나': 300}일때, 오렌지 3개, 사과 2개, 바나나 5개를 샀다면 총 구매액은??

fruits = {'오렌지': 400, '사과': 200, '바나나': 300}
print('fruits = ', fruits)
result = fruits['오렌지'] * 4 + fruits['사과'] * 2 + fruits['바나나'] * 5
print('오렌지 3개, 사과 2개, 바나나 5개 구매금액 = fruits["오렌지"] * 4 + fruits["사과"] * 2 + fruits["바나나"] * 5  = ', result)


## Introducing Python 3. list,tuple,dictionary,set
### 3.1 출생년도에 대한 year_lists를 만들어라. 1980년에서 1년씩 증가하여 다섯 번째 년도까지 넣어라.
year_lists = [1980, 1981, 1982, 1983, 1984, 1985]
print('year_lists = ', year_lists)
### 3.2 year_lists의 세 번째 생일년도는 무엇인가?
print('year_lists[3] = ', year_lists[3])
### 3.3 year_lists 중 가장 나이가 많을 때의 년도는?
print('year_lists[len(year_list)] = ', year_lists[len(year_lists) - 1])
print('year_lists[-1] = ', year_lists[-1])

### 3.4 "mozzarella", "cinderella", "salmonella"를 요소로 가지는 things 리스트를 만들어라.
things = ["mozzarella", "cinderella", "salmonella"]
print('things = ', things)
### 3.5 things 리스트에서 사람 이름의 첫 글자를 대문자로 바꿔서 출력하라.
things[1] = things[1].capitalize()
print('things = ', things)
### 3.6 things 리스트의 치즈 요소를 모두 대문자로 바꿔서 출력하라.
things[0] = things[0].upper()
print('things = ', things)
### 3.7 things 리스트의 질병 요소가 있다면 제거한 뒤 리스트를 출력하라.
things.pop()
print('things = ', things)

### 3.8 "Groucho", "Chico", "Harpo"를 요소로 가지는 surprise 리스트를 만들어라.
surprise = ["Groucho", "Chico", "Harpo"]
### 3.9 surprise 리스트의 마지막 요소를 소문자로 변경하고, 단어를 역전시키후, 첫 글자를 대문자로 바꿔라.
surprise[-1] = surprise[-1][::-1].lower()   ## :: means 'every'
surprise[-1].capitalize()
print('thing = ', things)

### 3.10 영어-프랑스어 사전을 만들어라.
e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}
### 3.11 사전에서 영어 walrus를 프랑스어로 출력하라.
print("English word 'dog' in Franch is {}".format(e2f["dog"]))
### 3.12 영불사전에서 불영사전을 만들어라.
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print('f2e = ', f2e)
### 3.13 불영사전을 이용하여 불어 chien의 영단어를 출력하라.
print('f2e["chien"] = ', f2e["chien"])
### 3.14 영불사전에서 영어단어 키를 출력하라.
print('e2f.keys() = ', e2f.keys())

### 3.15 2차원 딕셔너리 life를 만들어라. 최상위 키는 "animals", "plants", "other"이다. 그리고 "animal"은 각각 "cats", "octopi", "emus"를 키로 하고, "Henri", "Grumpy", "Lucy"를 값으로 한다. 나머지 요소는 빈 딕셔너리를 참조한다.
life = { "animals" : { "cats" : { "Henri" , "Grumpy", "Lucy"} , "octopi" : {} , "emus" : {} }, "plants" : {} , "other" : {} }
### 3.16 life 딕셔너리의 최상위 키를 출력하라.
print('life.keys() = ', life.keys())
### 3.17 life["animals"]의 모든 키를 출력하라.
print('life["animals"].keys() = ', life["animals"].keys())
### 3.18 life["animals"]["cats"]의 모든 값을 출력하라.
print('life["animals"]["cats"] = ', life["animals"]["cats"])