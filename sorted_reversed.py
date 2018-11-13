numbers = [1, 3, 4, 5, 2]
print("numbers = ", numbers)

sort_numbers = sorted(numbers)
print("sort_numbers = ", sort_numbers)
reverse_numbers = reversed(numbers)
print("revers_numbers = ", reverse_numbers)
print("numbers = ", numbers)

numbers.sort()
print("asc >> ", numbers)

numbers.sort(reverse=True)
print("desc >> ", numbers)

strs = ["aaa", "ccc", "한글", "세종대왕", "bbb",]
print("strs = ", sorted(strs))

t = (1, 5, 3)
print("t = ", sorted(t))