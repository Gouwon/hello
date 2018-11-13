def quadraple(n):
    return n * 4

numbers = (1, 2, 3, 4)
print(type(numbers))

quadraple_numbers = map(lambda x: x * 4, numbers)
print("quadraple_numbers using lambda = ", list(quadraple_numbers))

quadraple_numbers = map(quadraple, numbers)
print("quadraple_numbers using map = ", list(quadraple_numbers))