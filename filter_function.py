int_numbers = range(-10, 10)
print(list(int_numbers))

positives = filter(lambda x: x > 0, int_numbers)
print(list(positives))

def isNegatives(x):
    return x < 0

negatives = filter(isNegatives, int_numbers)
print(list(negatives))

# def filter(l):
#     ret = []
#     for i in l:
#         if i:
#             ret.append(i)
#         return ret
