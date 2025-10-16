my_list = [1, 2, 3, 4, 5]

#simple unpacking
a, b, c, d, e = my_list

print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

#skipping some values
a, _, c, _, e = my_list
print(f"a = {a}, c = {c}, e = {e}")

#unpack the first element and the rest inside a list
a, *b = my_list
print(f"a = {a}, b = {b}")

*a, b = my_list
print(f"a = {a}, b = {b}")

*a, b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")

first, *middle, last = my_list
# * gives us a list despite the type of mutable object. either we have a list or a tupple
# my_list = [1, 2, 3] returns first = 1 , middle = [2], last = 3
# my_list = [1, 2] returns first = 1 , middle = [], last = 2
print(f"1st element = {first}, middle part = {middle}, last element = {last}")