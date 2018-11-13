from functools import reduce

lst = [1, 2, 3, 4]
product = lst[0]
for i, num in enumerate(lst):
    if i == 0:
        continue
    product = product * num
print("product 1 >> ", product)

product2 = reduce(lambda x, y: x * y, lst)
print("product 2 >> ", product2)
# reduce의 첫번째 초기값은 받는 값의 1번째값으로 지정된다.