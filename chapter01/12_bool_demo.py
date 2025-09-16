a = True
b = False

print(type(a), a, sep=", ")
print(type(b), b, sep=", ")

#short circuit
result = a or b
print(result)

print("True + True =", True + True) #True + True = 2
print(True * 5)