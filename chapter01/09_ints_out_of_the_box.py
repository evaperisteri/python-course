a = 10
b = 20

result = a + b
print(f'{a} + {b} = {result}')

print("-----------")
print("Type of a:", type(a))
print(f"Type of a: {type(a)}")

magic_result = a.__add__(b)
print(f"Magic result: {magic_result}")