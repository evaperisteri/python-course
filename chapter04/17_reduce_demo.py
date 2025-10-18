from functools import reduce

# list of nums (ints)
my_ints = [1, 2, 3, 4 ,5]
result = reduce(lambda x, y : x + y, my_ints)
print(result)

result2 = reduce(lambda a, b : a * b, my_ints)
print(result2)

result3 = reduce(lambda a, b : a * b, my_ints, 100) # last value(100) * result
print(result3)