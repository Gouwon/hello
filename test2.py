# import re
# l = ['s[1]', 's[2]', 's[11]', 's[14]']

# pattern = "[0-9]"
# ll = re.findall(pattern, l[0])

# print(ll)

d = { "11" : 1, "22" : 2, "33" : 3}
print(len(d))
sort_keys = sorted(d.values())
data = {}
print(sort_keys)

i = 0
for k in sort_keys:
    if k not in data.values():
        id = "col_" + str(i)
        data[id] = k
        i += 1
print(data)