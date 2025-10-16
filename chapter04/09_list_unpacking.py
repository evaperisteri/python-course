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

print(f"1st element = {first}, middle part = {middle}, last element = {last}")