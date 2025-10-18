numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = list(range(1, 11))

# even number
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(type(even_numbers)) # filter object... an iterator

for num in even_numbers:
    print(num, end=" ")
print()

# print(*even_numbers)
# print(*even_numbers) we cant reprint an iterator 


even_num_list = list(filter(lambda x : x % 2 == 0, numbers))
print(even_num_list)

def even_num_func(n):
    return n % 2 == 0

my_list = list(filter(even_num_func, numbers))
print(my_list)