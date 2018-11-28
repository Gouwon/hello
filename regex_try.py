import re

python_str = """The Zen of Python
Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

## is better than을 기준으로 (.*) ugly가 나오는가?
# st = "Beautiful is better than ugly."

# aw = re.findall("is better than (.*).", st)
# print(aw)
# bw = re.findall("(.*) is better than", st)
# print(bw)

# pattern1 = re.compile("is better than (.*).")
# # pattern2 = re.compile("(.*) is better than")
# pattern3 = re.compile("(.*) is better than (.*).")


# mm = re.findall("is better than (.*)\.$", python_str, re.MULTILINE)
# print(type(mm), mm)
# mm1 = re.findall("(.*) is better than", python_str, re.MULTILINE)
# print(type(mm1), mm1)
# for i, v in enumerate(mm):
#     print("{} > {}".format(mm1[i], mm[i]))



## 마침표 이후 개행이 없는 라인에 개행 추가
# s = re.sub("\.[^\n]", '.\n', s)

# patterns = re.compile("(.*) is better than (.*).")
# m = re.findall("(.*) is better than (.*)\.", python_str)
m = re.findall("(.*) is.* better than (.*)\.", python_str)
for i in m:
    print("{} > {}".format(i[0].lower(), i[1]))

# m2 = re.finditer(patterns, python_str)
# for i in m2:
#     print(i.group(1), i.group(2))



# string = "Beautiful is better than ugly. Explicit is better than implicit."

# m = re.findall("(.*) is better than (.*)\.\s", string)
# print("Ccccccccccc", m)