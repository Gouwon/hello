import re
line = "Beautiful is better than ugly."
# matches = re.findall("Be", line)
# print(matches)

# matches2 = re.findall("Be", line, re.IGNORECASE)
# print(matches2)

# zen2 = """Although never is often better than * right * now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea - - let's do more of those!"""

# m = re.findall("^If", zen2, re.MULTILINE)
# m2 = re.findall("idea\.", zen2, re.MULTILINE)
# m22 = re.findall("idea.*", zen2, re.MULTILINE)
# m3 = re.findall("idea.$", zen2, re.MULTILINE)
# m33 = re.findall("idea.", zen2, re.MULTILINE)
# m333 = re.findall("idea", zen2, re.MULTILINE)
# print(m, m2, m22, m3, m33, m333)

# string = "Two aa too"

# # m = re.findall("t[ow]o", string)
# m = re.findall("t[ow]o", string, re.IGNORECASE)
# print(m)


# m = re.findall("t[^w]o", string, re.IGNORECASE)
# print(m)

# string = "123?45yy7890 hi 999 hello"


# m1 = re.findall("\d", string)
# m2 = re.findall("[0-9]{1,2}", string)
# m3 = re.findall("[1-5]{1,2}", string)
# m4 = re.findall("[A-z]{1,2}", string)

# print("m1=", m1)
# print("m2=", m2)
# print("m3=", m3)
# print("m4=", m4)

# string = "aaaaaaa<hr>This"

# pattern = re.compile("<(.*)>")         cf. re.compile("<.*>")

# mm = re.findall(pattern, string)
# print(mm)

# for m in re.finditer(pattern, string):
#     print(m.groups(1))