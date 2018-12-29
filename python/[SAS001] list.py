str_list = "camus"

for i in str_list[0:len(str_list)]:
    print(i)

## 3.(1) 키, 좋아하는 색깔, 좋아하는 작가 등 당신에 관해 설명하는 딕셔너리를 만드시오.
dict_list = {"키" : 176, "색깔" : "검정", "작가" : "유병재"}

## (2) 사용자에게 키, 좋아하는 색깔, 좋아하는 작가 등을 묻고 (1)에서 만든 딕셔너리에서 그 답을 찾아 반환하는 프로그램을 만드시오.
user_input = input('당신이 좋아하는 것을 알려드립니다. \nusage) "키" or "색깔" or "작가" >>> ')
if user_input == "키":
    print("당신의 {}는 {:d}입니다.".format(user_input, dict_list[user_input]))
elif user_input == "색깔":
    print("당신의 {}는 {}입니다.".format(user_input, dict_list[user_input]))
else:
    print("당신의 {}는 {}입니다.".format(user_input, dict_list[user_input]))